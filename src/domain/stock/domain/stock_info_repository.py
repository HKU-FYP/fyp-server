from sqlalchemy.orm import Session

from src.domain.stock.domain.model.stock_info import StockInfo


class StockInfoRepository:

    def get_all_stock_info(self, session: Session):
        return session.query(StockInfo).all()

    def find_by_ticker(self, session: Session, ticker: str) -> StockInfo:
        return session.query(StockInfo).filter(StockInfo.ticker == ticker).first()

    def find_by_id(self, session: Session, stock_info_id: int) -> StockInfo:
        return session.query(StockInfo).filter(StockInfo.id == stock_info_id).first()
