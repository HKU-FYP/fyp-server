from src.domain.member.application.member_service import MemberService
from src.domain.member.domain.member_repository import MemberRepository
from src.domain.sample.application.sample_service import SampleService
from src.domain.stock.application.stock_info_service import StockInfoService
from src.domain.stock.domain.stock_info_repository import StockInfoRepository

# Sample
sample_service = SampleService()

# Member
member_repository = MemberRepository()
member_service = MemberService(member_repository)

# Stock
stock_info_repository = StockInfoRepository()
stock_info_service = StockInfoService(stock_info_repository)
