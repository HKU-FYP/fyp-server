from sqlalchemy.orm import Session

from src.domain.stock.domain.user_stock_repository import UserStockRepository
from src.domain.user.application.dto.response.check_user_stock_exist_response import (
    CheckUserStockExistResponseDto,
)
from src.domain.user.application.dto.response.login_response import LoginResponseDto
from src.domain.user.application.dto.response.signup_response import SignUpResponseDto
from src.domain.user.domain.model.user import User
from src.domain.user.domain.user_repository import UserRepository
from src.shared.exception.base import BaseCustomException
from src.shared.utils.auth_util import (
    check_password,
    create_access_token,
    hash_password,
)


class UserService:
    def __init__(self, user_repository: UserRepository, user_stock_repository: UserStockRepository):
        self.user_repository = user_repository
        self.user_stock_repository = user_stock_repository

    def signup(self, username: str, password: str, session):
        # Check if username already exists
        user = self.user_repository.find_by_username(username, session)
        if user:
            raise BaseCustomException(status_code=400, detail="Username already exists.")

        # Hash password
        hashed_password = hash_password(password)

        user = User(username=username, password=hashed_password)
        self.user_repository.save(user, session)
        return SignUpResponseDto(user_id=user.id)

    def login(self, username: str, password: str, session):
        user = self.user_repository.find_by_username(username, session)

        # Check if user exists
        if not user:
            raise BaseCustomException(status_code=400, detail="Invalid username or password.")

        # Check if password is correct
        if not check_password(raw_password=password, hashed_password=user.password):
            raise BaseCustomException(status_code=400, detail="Invalid username or password.")

        # Issue JWT token
        token = create_access_token(sub=user.id)
        return LoginResponseDto(access_token=token)

    def is_user_stock_exist(self, session: Session, user_id: int):
        user_stocks = self.user_stock_repository.find_all_by_user_id(session, user_id)
        exist = len(user_stocks) > 0
        return CheckUserStockExistResponseDto(exist=exist)
