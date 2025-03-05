from sqlalchemy.orm import Session
from src.domain.news.domain.models.news import News


class NewsRepository:

    def save(self, session: Session, news: News):
        session.add(news)
        session.commit()

    def find_all_by_user_stock_id(self, session: Session, user_stock_id: int) -> list[News]:
        return session.query(News).filter(News.user_stock_id == user_stock_id).all()

    def find_by_id(self, session: Session, news_id: int) -> News:
        return session.query(News).filter(News.id == news_id).one()
