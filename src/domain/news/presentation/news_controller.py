from fastapi import APIRouter, Depends, status

from src.shared.database.session import get_session
from src.shared.utils.auth_util import get_current_user_id
from src.domain.news.application.dto.response.GetAllNewsbyUserStockIdResponseDto import (
    GetAllNewsByUserStockIdResponseDto,
)
from src.domain.di_container import news_service

router = APIRouter(tags=["News"])


@router.get("/user-stocks/{user_stock_id}/news", status_code=status.HTTP_200_OK)
def get_all_news_by_user_stock_id(
    user_stock_id: int, session=Depends(get_session)
):
    return news_service.get_all_news_by_user_stock_id(session, user_stock_id)

@router.get("/news/{news_id}", status_code=status.HTTP_200_OK)
def get_news_info_by_id(news_id: int, session=Depends(get_session)):
    return news_service.get_news_by_id(session, news_id)
