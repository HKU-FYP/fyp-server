import requests
from sqlalchemy.orm import Session

from src.config import load_config
from src.domain.stock.application.dto.response.get_stock_info_response import (
    GetStockInfoResponseDto,
    StockInfoDto,
)
from src.domain.stock.application.dto.response.GetStockDetailInfoByTickerResponseDto import (
    GetStockDetailInfoByTickerResponseDto,
)
from src.domain.stock.application.stock_info_fetcher import StockInfoFetcher
from src.domain.stock.domain.stock_info_repository import StockInfoRepository

cfg = load_config()


class StockInfoService:
    def __init__(self, stock_info_repository: StockInfoRepository, stock_info_fetcher: StockInfoFetcher):
        self.stock_info_repository = stock_info_repository
        self.stock_info_fetcher = stock_info_fetcher

    def get_all_stock_info(self, session: Session) -> GetStockInfoResponseDto:
        stocks = self.stock_info_repository.get_all_stock_info(session)
        return GetStockInfoResponseDto(
            stocks=[StockInfoDto(id=stock.id, ticker=stock.ticker, name=stock.name) for stock in stocks]
        )

    def get_stock_info_detail_by_ticker(self, ticker: str) -> GetStockDetailInfoByTickerResponseDto:
        # Stock Detail Info
        return self.stock_info_fetcher.get_stock_info_detail_by_ticker(ticker)
