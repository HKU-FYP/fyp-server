from sqlalchemy.orm import Session

from src.domain.stock.application.dto.response.get_user_stocks_response import (
    UserStockInfoDto,
)
from src.domain.stock.domain.model.user_stock import UserStock
from src.domain.stock.domain.stock_info_repository import StockInfoRepository
from src.domain.stock.domain.user_stock_repository import UserStockRepository
from src.shared.exception.base import BaseCustomException


class UserStockService:
    def __init__(self, user_stock_repository: UserStockRepository, stock_info_repository: StockInfoRepository):
        self.user_stock_repository = user_stock_repository
        self.stock_info_repository = stock_info_repository

    def save_user_stock(self, session: Session, user_id: int, stock_info_id: int):
        # Check whether the user already input a stock with the same stock_info_id
        user_stocks = self.user_stock_repository.find_all_by_user_id(session, user_id)
        if user_stocks:
            raise BaseCustomException(400, "User already has the stock")

        user_stock = UserStock(user_id=user_id, stock_info_id=stock_info_id)
        self.user_stock_repository.save(session, user_stock)

    def get_user_stocks_by_user_id(self, session: Session, user_id: int) -> list[UserStockInfoDto]:
        user_stocks = self.user_stock_repository.find_all_by_user_id(session, user_id)
        res = []
        for user_stock in user_stocks:
            stock_info = self.stock_info_repository.find_by_id(session, user_stock.stock_info_id)
            res.append(UserStockInfoDto(id=user_stock.stock_info_id, ticker=stock_info.ticker, name=stock_info.name))

        return res
