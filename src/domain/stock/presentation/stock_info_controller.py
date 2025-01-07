from fastapi import APIRouter, Depends, status
from src.shared.utils.auth_util import get_current_user_id
from src.shared.database.session import get_session
from src.domain.di_container import stock_info_service

from src.domain.stock.application.dto.response.get_stock_info_response import GetStockInfoResponseDto


router = APIRouter(tags=["Stock Info"])

@router.get("/all-stock-ticker-info", status_code=status.HTTP_200_OK, response_model=GetStockInfoResponseDto)
def get_all_stock_ticker_info(
    session=Depends(get_session),
    user_id: int = Depends(get_current_user_id)
) -> GetStockInfoResponseDto:
    return stock_info_service.get_all_stock_info(session)