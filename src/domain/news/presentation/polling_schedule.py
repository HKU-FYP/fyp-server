from apscheduler.schedulers.background import BackgroundScheduler
import requests
import json
from pprint import pprint
from pymilvus import MilvusClient, model

from src.domain.news.application.sentiment_analyzer import NewsArticleDto, \
    SentimentAnalysisResultDto
from src.domain.news.application.stock_impact_analyzer import \
    StockImpactAnalysisResultDto
from src.domain.news.application.summary_generator import \
    SummaryGenerationResponseDto
from src.domain.news.domain.models.metric import Metric
from src.domain.news.domain.models.news import News
from src.domain.di_container import news_repository, sentiment_analyzer, \
    user_stock_repository, stock_info_repository, financial_metric_analyzer, \
    metric_repository, stock_impact_analyzer
from datetime import datetime
from src.shared.database.session import get_session
from src.domain.di_container import summary_generator_llm
from src.shared.discord.discord_client import discord_client

client = MilvusClient("milvus_demo.db")
sentence_transformer = model.dense.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2", device="cpu")

idx = 0
total_len = 6

with open("news_data.json") as f:
    news_data_list = json.load(f)


def start_polling(threshold=0.4):
    threshold = 0.4
    global idx
    session = next(get_session())

    # News를 JSON 파일에서 polling한다 (1개씩) -> DTO로 변환
    news_data = news_data_list[idx]
    print(f"[idx: {idx}] {news_data['title']}")

    news_query_str = [
        news_data["summary"]
        # news_data['title']
    ]

    query_vectors = sentence_transformer.encode_queries(news_query_str)

    # Embedding Search 수행 (news contents <-> user input stock name)
    results = client.search(
        collection_name="dummy_demo1",
        anns_field="vector",
        data=query_vectors,
        limit=500,
        output_fields=["id", "stock_info_id", "ticker", "name", "keyword", "user_stock_id"],
        search_params={
            "metric_type": "COSINE",  # Match the index metric type
            "params": {"nprobe": 10},  # Number of clusters to search
        },
    )
    results = results[0]

    # 만약 threshold 넘는 result가 1개라도 있으면 Summary Generation 해야됨.
    is_matched_result = any([result["distance"] >= threshold for result in results])
    summary_dto = None
    key_metrics: list[str] = []

    results = [result for result in results if result['distance'] >= threshold]
    unique_results = {}
    for result in results:
        user_stock_id = result.get("user_stock_id")
        if (user_stock_id not in unique_results or
            result["distance"] > unique_results[user_stock_id]["distance"]):
            unique_results[user_stock_id] = result

    results = list(unique_results.values())
    print(results)

    if is_matched_result:
        # 1. Summary 생성
        # TODO: DUMMY FIX
        summary_dto = summary_generator_llm.generate_summary(content=news_data['summary'])
        # summary = "This is dummy summary to not waste tokens"
        # summary_dto = SummaryGenerationResponseDto("summary", "one-sentence-summary")

        # 2. Key metrics
        # key_metrics = ["abc", "edf", "zyx"]
        # TODO: DUMMY FIX
        key_metrics = financial_metric_analyzer.analyze_metrics(
            news_data['summary']).metrics
        print("Key Metrics: ", key_metrics)

    sentiment_analysis_cache: dict[str, SentimentAnalysisResultDto] = {}
    stock_impact_analysis_cache: dict[str, StockImpactAnalysisResultDto] = {}

    for result in results:
        distance = result["distance"]
        print("Distance:", distance)
        print()
        if distance < threshold:
            continue

        entity = result["entity"]
        print("Matched Keyword: ", entity["keyword"])
        datetime_obj = datetime.strptime(news_data["published_date"], "%Y-%m-%d %H:%M:%S")

        # 3. Sentiment Analysis -> stock이 유저마다 다를 수 있음.
        user_stock_id = entity['user_stock_id']
        user_stock = user_stock_repository.find_by_user_stock_id(session, user_stock_id)
        stock_info = stock_info_repository.find_by_id(session, user_stock.stock_info_id)
        stock_name: str = stock_info.name

        sentiment_analysis_result = None

        if stock_name in sentiment_analysis_cache:
            sentiment_analysis_result = sentiment_analysis_cache[stock_name]
        else:
            # TODO: DUMMY FIX
            # sentiment_analysis_result = SentimentAnalysisResultDto(
            #     sentiment="Positive",
            #     sentiment_score=2.23,
            #     analysis="Dummy Analysis Placeholder to save tokens"
            # )
            sentiment_analysis_result = sentiment_analyzer.analyze_sentiment(
                NewsArticleDto(news_data['title'], news_data['summary']),
                stock_name
            )

        stock_impact_analysis_result = None

        if stock_name in stock_impact_analysis_cache:
            stock_impact_analysis_result = stock_impact_analysis_cache[stock_name]
        else:
            # TODO: DUMMY FIX
            stock_impact_analysis_result: StockImpactAnalysisResultDto = stock_impact_analyzer.analyze_stock_impact(stock_name, news_data['summary'])
            # stock_impact_analysis_result = StockImpactAnalysisResultDto(easy="dummy easy", intermediate="dummy intermediate", expert="dummy expert")


        print(sentiment_analysis_result)
        print("-" * 50)
        print("[Stock Impact Analysis]")
        print(stock_impact_analysis_result)
        print("-" * 50)

        news = News(
            user_stock_id=entity["user_stock_id"],
            matched_keyword=entity['keyword'],
            title=news_data["title"],
            author=news_data["author"],
            published_date=datetime_obj,
            link=news_data["link"],
            publisher=news_data["clean_url"],
            content=news_data["summary"],
            summary=summary_dto.summary,
            one_sentence_summary=summary_dto.one_sentence_summary,
            sentiment=sentiment_analysis_result.sentiment,
            sentiment_score=sentiment_analysis_result.sentiment_score,
            sentiment_analysis=sentiment_analysis_result.analysis,
            stock_impact_analysis_easy=stock_impact_analysis_result.easy,
            stock_impact_analysis_intermediate=stock_impact_analysis_result.intermediate,
            stock_impact_analysis_expert=stock_impact_analysis_result.expert,
        )

        discord_client.report_news(stock_name, news.title, summary_dto.summary, datetime_obj.strftime("%Y-%m-%d %H:%M:%S"), news.sentiment)

        news_repository.save(session, news)

        for metric in key_metrics:
            metric_repository.save(session, Metric(metric_content=metric, news_id=news.id))

    idx = (idx + 1) % total_len
