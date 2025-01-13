from src.config import load_config
from src.domain.sample.application.sample_service import SampleService
from src.domain.stock.application.stock_info_fetcher import StockInfoFetcher
from src.domain.stock.application.stock_info_service import StockInfoService
from src.domain.stock.application.user_stock_service import UserStockService
from src.domain.stock.domain.stock_info_repository import StockInfoRepository
from src.domain.stock.domain.user_stock_repository import UserStockRepository
from src.domain.user.application.user_service import UserService
from src.domain.user.domain.user_repository import UserRepository

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
