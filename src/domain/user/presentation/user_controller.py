from fastapi import APIRouter, Depends, status

from src.shared.utils.auth_util import get_current_user_id
from src.domain.di_container import user_service
from src.domain.di_container import user_stock_service
from src.domain.user.application.dto.request.login_request import LoginRequestDto
from src.domain.user.application.dto.request.signup_request import SignUpRequestDto
from src.domain.user.application.dto.response.login_response import LoginResponseDto
from src.domain.user.application.dto.response.signup_response import SignUpResponseDto
from src.domain.user.application.dto.response.check_user_stock_exist_response import CheckUserStockExistResponseDto
from src.domain.stock.application.dto.response.get_user_stocks_response import UserStockInfoDto
from src.shared.database.session import get_session

router = APIRouter(tags=["User"])


@router.post("/signup", status_code=status.HTTP_200_OK, response_model=SignUpResponseDto)
def signup(request: SignUpRequestDto, session=Depends(get_session)):
    return user_service.signup(username=request.username, password=request.password, session=session)


@router.post("/login", status_code=status.HTTP_200_OK, response_model=LoginResponseDto)
def login(request: LoginRequestDto, session=Depends(get_session)):
    return user_service.login(username=request.username, password=request.password, session=session)


@router.get("/secure", status_code=status.HTTP_200_OK)
def get_secure(user_id: int = Depends(get_current_user_id)):
    return {"current_user_id": user_id}

@router.get("/users/exist-user-stock", status_code=status.HTTP_200_OK, response_model=CheckUserStockExistResponseDto)
def check_has_user_input_stock(user_id: int = Depends(get_current_user_id), session = Depends(get_session)) -> CheckUserStockExistResponseDto:
    return user_service.is_user_stock_exist(session=session, user_id=user_id)

@router.get("/users/stocks", status_code=status.HTTP_200_OK)
def get_user_stocks(user_id: int = Depends(get_current_user_id), session = Depends(get_session)) -> list[UserStockInfoDto]:
    return user_stock_service.get_user_stocks_by_user_id(session, user_id)