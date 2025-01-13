import random
import string
from datetime import datetime, timedelta

import bcrypt
import jwt
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jwt.exceptions import (
    ExpiredSignatureError,
    InvalidSignatureError,
    InvalidTokenError,
)

from src.config import load_config
from src.shared.exception.base import BaseCustomException

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/login", scheme_name="JWT")

cfg = load_config()


def hash_password(raw_password: str) -> str:
    """Hashes a password using bcrypt."""
    return bcrypt.hashpw(raw_password.encode(), bcrypt.gensalt()).decode()


def check_password(raw_password: str, hashed_password: str) -> bool:
    """Checks if a password matches its hash."""
    return bcrypt.checkpw(raw_password.encode(), hashed_password.encode())


def create_access_token(sub: str | int) -> str:
    payload = {
        "sub": str(sub),
        "scope": "access_token",
        "exp": datetime.utcnow() + timedelta(minutes=100000),
        "iat": datetime.utcnow(),
    }

    return jwt.encode(payload, cfg.jwt.secret_key, algorithm="HS256")


def decode_token(token: str) -> str:
    try:
        payload = jwt.decode(token, cfg.jwt.secret_key, algorithms=["HS256"])
        sub = payload["sub"]
        return sub
    except ExpiredSignatureError:
        raise BaseCustomException(status_code=401, detail="Token has expired.")
    except InvalidSignatureError:
        raise BaseCustomException(status_code=401, detail="Token signature is invalid.")
    except InvalidTokenError:
        raise BaseCustomException(status_code=401, detail="Token is invalid.")


def get_current_user_id(token: str = Depends(oauth2_scheme)) -> int:
    try:
        a = decode_token(token)
        return int(decode_token(token))
    except Exception:
        raise BaseCustomException(status_code=401, detail="Invalid token.")
