from typing import List

from sqlalchemy.orm import Session

from src.domain.news.domain.models.metric import Metric


class MetricRepository:

    def save(self, session: Session, metric: Metric):
        session.add(metric)
        session.commit()

    def find_all_by_news_id(self, session: Session, news_id: int) -> List[Metric]:
        return session.query(Metric).filter(Metric.news_id == news_id).all()