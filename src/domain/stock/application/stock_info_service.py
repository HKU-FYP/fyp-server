from sqlalchemy.orm import Session
from src.domain.stock.domain.stock_info_repository import StockInfoRepository
from src.domain.stock.application.dto.response.get_stock_info_response import GetStockInfoResponseDto, StockInfoDto


class StockInfoService:
    def __init__(self, stock_info_repository: StockInfoRepository):
        self.stock_info_repository = stock_info_repository
    
    def get_all_stock_info(self, session: Session) -> GetStockInfoResponseDto:
        stocks = self.stock_info_repository.get_all_stock_info(session)
        return GetStockInfoResponseDto(
            stocks=[StockInfoDto(id=stock.id, ticker=stock.ticker, name=stock.name) for stock in stocks]
        )
