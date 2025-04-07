from pydantic import BaseModel


class GetDashboardSummaryResponseDto(BaseModel):
    positive_summary_list: list[str]
    negative_summary_list: list[str]