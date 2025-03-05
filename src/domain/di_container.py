from src.config import load_config
from src.domain.news.application.FinancialMetricsAnalyzer import \
    FinancialMetricAnalyzer
from src.domain.news.application.sentiment_analyzer import SentimentAnalyzer
from src.domain.news.application.stock_impact_analyzer import \
    StockImpactAnalyzer
from src.domain.news.application.summary_generator import SummaryGeneratorLLM
from src.domain.news.domain.metric_repository import MetricRepository
from src.domain.sample.application.sample_service import SampleService
from src.domain.stock.application.stock_info_fetcher import StockInfoFetcher
from src.domain.stock.application.stock_info_service import StockInfoService
from src.domain.stock.application.user_stock_service import UserStockService
from src.domain.stock.domain.stock_info_repository import StockInfoRepository
from src.domain.stock.domain.user_stock_repository import UserStockRepository
from src.domain.user.application.user_service import UserService
from src.domain.user.domain.user_repository import UserRepository
from src.domain.news.domain.news_repository import NewsRepository
from src.domain.news.application.news_service import NewsService
from pymilvus import MilvusClient

from src.shared.llm.openai_llm import OpenAIChatLLM

cfg = load_config()

# Sample
sample_service = SampleService()

# Stock
stock_info_fetcher = StockInfoFetcher(api_key=cfg.stock.api_key)
stock_info_repository = StockInfoRepository()
stock_info_service = StockInfoService(stock_info_repository, stock_info_fetcher)

user_stock_repository = UserStockRepository()
user_stock_service = UserStockService(user_stock_repository, stock_info_repository)

# User
user_repository = UserRepository()
user_service = UserService(user_repository, user_stock_repository)

# News
metric_repository = MetricRepository()
llm = OpenAIChatLLM(api_key=cfg.openai.api_key)
summary_generator_llm = SummaryGeneratorLLM(llm=llm)
news_repository = NewsRepository()
news_service = NewsService(news_repository, metric_repository)
sentiment_analyzer = SentimentAnalyzer(llm=llm)
financial_metric_analyzer = FinancialMetricAnalyzer(llm=llm)
stock_impact_analyzer = StockImpactAnalyzer(llm=llm)
# Milvus
# milvus_client = MilvusClient(
#     uri="http://localhost:19530",
#     token="root:Milvus"
# )
