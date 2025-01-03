from src.domain.member.domain.member_repository import MemberRepository
from src.domain.member.domain.model.member import Member


class MemberService:
    def __init__(self, member_repository: MemberRepository):
        self.member_repository = member_repository

    async def signup(self, username: str, password: str, session):
        member = Member(username=username, password=password)
        self.member_repository.save(member, session)