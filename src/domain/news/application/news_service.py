from src.domain.news.application.dto.response.GetDashboardNewsSummaryResponseDto import \
    GetDashboardSummaryResponseDto
from src.domain.news.application.dto.response.GetNewsByIdResponseDto import \
    GetNewsByIdResponseDto
from src.domain.news.domain.metric_repository import MetricRepository
from src.domain.news.domain.news_repository import NewsRepository
from src.domain.news.application.dto.response.GetAllNewsbyUserStockIdResponseDto import (
    GetAllNewsByUserStockIdResponseDto,
)
from sqlalchemy.orm import Session


class NewsService:
    def __init__(self, news_repository: NewsRepository, metric_repository: MetricRepository):
        self.news_repository = news_repository
        self.metric_repository = metric_repository

    def get_dashboard_summary(self, session: Session, user_stock_id: int) -> GetDashboardSummaryResponseDto:
        # Get all news by user_stock_id
        news_list = self.news_repository.find_all_by_user_stock_id(session, user_stock_id)

        positive_news_list = [news for news in news_list if news.sentiment == 'Positive' or news.sentiment == 'Strong_Positive']
        positive_news_list.sort(key=lambda x: x.sentiment_score, reverse=True)
        positive_news_list = positive_news_list[:3]
        positive_summary_list = [news.one_sentence_summary for news in positive_news_list]

        negative_news_list = [news for news in news_list if news.sentiment == 'Negative' or news.sentiment == 'Strong_Negative']
        negative_news_list.sort(key=lambda x: x.sentiment_score)
        negative_news_list = negative_news_list[:3]
        negative_summary_list = [news.one_sentence_summary for news in negative_news_list]

        return GetDashboardSummaryResponseDto(
           positive_summary_list=positive_summary_list,
            negative_summary_list=negative_summary_list,
        )

    def get_all_news_by_user_stock_id(self, session: Session, user_stock_id: int) -> GetAllNewsByUserStockIdResponseDto:
        news_list = self.news_repository.find_all_by_user_stock_id(session, user_stock_id)

        return [
            GetAllNewsByUserStockIdResponseDto(
                id=news.id,
                title=news.title,
                author=news.author,
                published_date=news.published_date,
                link=news.link,
                publisher=news.publisher,
                content=news.content,
                sentiment=news.sentiment
            )
            for news in news_list
        ]

    def get_news_by_id(self, session: Session, news_id: int) -> GetNewsByIdResponseDto:
        news = self.news_repository.find_by_id(session, news_id)
        if not news:
            raise Exception("No News found")

        metrics = self.metric_repository.find_all_by_news_id(session, news_id)

        return GetNewsByIdResponseDto(
            id=news.id,
            title=news.title,
            author=news.author,
            published_date=news.published_date,
            link=news.link,
            publisher=news.publisher,
            content=news.content,
            summary=news.summary,
            one_sentence_summary=news.one_sentence_summary,
            sentiment=news.sentiment,
            sentiment_analysis=news.sentiment_analysis,
            stock_impact_analysis_easy=news.stock_impact_analysis_easy,
            stock_impact_analysis_intermediate=news.stock_impact_analysis_intermediate,
            stock_impact_analysis_expert=news.stock_impact_analysis_expert,
            key_metrics=[metric.metric_content for metric in metrics]
        )


