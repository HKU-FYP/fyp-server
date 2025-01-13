from sqlalchemy.orm import Session

from src.domain.user.domain.model.user import User


class UserRepository:

    def save(self, user: User, session: Session):
        session.add(user)
        session.commit()
        session.refresh(user)
        return user

    def find_by_username(self, username: str, session: Session):
        return session.query(User).filter(User.username == username).first()
