from src.domain.member.application.dto.response.login_response import LoginResponseDto
from src.domain.member.application.dto.response.signup_response import SignUpResponseDto
from src.domain.member.domain.member_repository import MemberRepository
from src.domain.member.domain.model.member import Member
from src.shared.exception.base import BaseCustomException
from src.shared.utils.auth_util import (
    check_password,
    create_access_token,
    hash_password,
)


class MemberService:
    def __init__(self, member_repository: MemberRepository):
        self.member_repository = member_repository

    def signup(self, username: str, password: str, session):
        # Check if username already exists
        member = self.member_repository.find_by_username(username, session)
        if member:
            raise BaseCustomException(status_code=400, detail="Username already exists.")

        # Hash password
        hashed_password = hash_password(password)

        member = Member(username=username, password=hashed_password)
        self.member_repository.save(member, session)
        return SignUpResponseDto(member_id=member.id)

    def login(self, username: str, password: str, session):
        member = self.member_repository.find_by_username(username, session)

        # Check if member exists
        if not member:
            raise BaseCustomException(status_code=400, detail="Invalid username or password.")

        # Check if password is correct
        if not check_password(raw_password=password, hashed_password=member.password):
            raise BaseCustomException(status_code=400, detail="Invalid username or password.")

        # Issue JWT token
        token = create_access_token(sub=member.id)
        return LoginResponseDto(access_token=token)
