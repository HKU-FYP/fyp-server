from apscheduler.schedulers.background import BackgroundScheduler
import requests
import json
from pprint import pprint
from pymilvus import MilvusClient, model

client = MilvusClient("milvus_demo.db")
sentence_transformer = model.dense.SentenceTransformerEmbeddingFunction(
    model_name='all-MiniLM-L6-v2', 
    device='cpu' 
)

idx = 0
total_len = 8

with open("news_data.json") as f:
    news_data_list = json.load(f)

def start_polling():
    global idx

    # News를 .json에 저장되어있음 (OK)

    # News를 JSON 파일에서 polling한다 (1개씩) -> DTO로 변환
    news_data = news_data_list[idx]

    news_query_str = [
        news_data['summary']
    ]

    query_vectors = sentence_transformer.encode_queries(news_query_str)

    # Embedding Search 수행 (news contents <-> user input stock name)
    res = client.search(
        collection_name="dummy_demo1", 
        data=query_vectors,
        limit=10,
        output_fields=['id', '']
    )

    # Output(stock_info_id 리스트)

    # user_stock entity에 요걸로 필터링 한다 -> user_stocks

    # 그러면 해당 user_stocks에다가 news FK 매핑해줌
    
    idx = (idx + 1) % total_len