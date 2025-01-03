from fastapi import APIRouter, Depends, status
from src.domain.di_container import member_service
from src.domain.member.application.dto.request.signup_request import SignUpRequestDto
from fastapi import Depends
from src.shared.database.session import get_session


router = APIRouter(tags=["Member"])

@router.post("/signup", status_code=status.HTTP_200_OK)
async def signup(request: SignUpRequestDto, session=Depends(get_session)):
    await member_service.signup(username=request.username, password=request.password, session=session)
