from sqlalchemy.orm import Session
from src.domain.stock.domain.model.user_stock import UserStock
from src.domain.stock.domain.user_stock_repository import UserStockRepository
from src.shared.exception.base import BaseCustomException

class UserStockService:
    def __init__(self, user_stock_repository: UserStockRepository):
        self.user_stock_repository = user_stock_repository
    
    def save_user_stock(self, session: Session, user_id: int, stock_info_id: int):
        # Check whether the user already input a stock with the same stock_info_id
        user_stocks = self.user_stock_repository.find_all_by_user_id(session, user_id)
        if user_stocks:
            raise BaseCustomException(400, "User already has the stock")

        user_stock = UserStock(user_id=user_id, stock_info_id=stock_info_id)
        self.user_stock_repository.save(session, user_stock)