from fastapi import APIRouter, Depends, status

from src.domain.di_container import user_stock_service
from src.domain.stock.application.dto.request.save_user_stock_request import (
    SaveUserStockRequestDto,
)
from src.shared.database.session import get_session
from src.shared.utils.auth_util import get_current_user_id

router = APIRouter(tags=["User Stock"])


@router.post("/users/stock", status_code=status.HTTP_201_CREATED)
def save_user_stock(
    request: SaveUserStockRequestDto, session=Depends(get_session), user_id: int = Depends(get_current_user_id)
):
    user_stock_service.save_user_stock(session, user_id, request.stock_info_id)
