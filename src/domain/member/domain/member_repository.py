from sqlalchemy.orm import Session

from src.domain.member.domain.model.member import Member


class MemberRepository:

    def save(self, member: Member, session: Session):
        session.add(member)
        session.commit()
        session.refresh(member)
        return member

    def find_by_username(self, username: str, session: Session):
        return session.query(Member).filter(Member.username == username).first()
