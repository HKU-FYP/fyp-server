from sqlalchemy.orm import Session
from src.domain.member.domain.model.member import Member

class MemberRepository:

    def save(self, member: Member, session: Session):
        session.add(member)
        session.commit()
        session.refresh(member)
        return member

