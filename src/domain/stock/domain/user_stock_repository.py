from typing import Type

from sqlalchemy.orm import Session

from src.domain.stock.domain.model.user_stock import UserStock


class UserStockRepository:

    def save(self, session: Session, user_stock: UserStock):
        session.add(user_stock)
        session.commit()

    def find_all_by_user_id(self, session: Session, user_id: int):
        return session.query(UserStock).filter(UserStock.user_id == user_id).all()

    def find_by_user_stock_id(self, session: Session, user_stock_id: int) -> Type[UserStock]:
        return session.query(UserStock).filter(UserStock.id == user_stock_id).one()
