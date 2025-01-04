from fastapi import APIRouter, Depends, status

from src.shared.utils.auth_util import get_current_user_id
from src.domain.di_container import member_service
from src.domain.member.application.dto.request.login_request import LoginRequestDto
from src.domain.member.application.dto.request.signup_request import SignUpRequestDto
from src.domain.member.application.dto.response.login_response import LoginResponseDto
from src.domain.member.application.dto.response.signup_response import SignUpResponseDto
from src.shared.database.session import get_session

router = APIRouter(tags=["Member"])


@router.post("/signup", status_code=status.HTTP_200_OK, response_model=SignUpResponseDto)
def signup(request: SignUpRequestDto, session=Depends(get_session)):
    return member_service.signup(username=request.username, password=request.password, session=session)


@router.post("/login", status_code=status.HTTP_200_OK, response_model=LoginResponseDto)
def login(request: LoginRequestDto, session=Depends(get_session)):
    return member_service.login(username=request.username, password=request.password, session=session)


@router.get("/secure", status_code=status.HTTP_200_OK)
def get_secure(user_id: int = Depends(get_current_user_id)):
    return {"current_user_id": user_id}