from sqlalchemy.orm import Session
from src.domain.stock.domain.model.stock_info import StockInfo


class StockInfoRepository:

    def get_all_stock_info(self, session: Session):
        return session.query(StockInfo).all()