from src.domain.sample.application.sample_service import SampleService
from src.domain.member.application.member_service import MemberService
from src.domain.member.domain.member_repository import MemberRepository

# Sample
sample_service = SampleService()

# Member
member_repository = MemberRepository()
member_service = MemberService(member_repository)
