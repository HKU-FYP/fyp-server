from src.shared.database.connection import SessionLocal
from contextlib import contextmanager


def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
