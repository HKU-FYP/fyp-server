from src.domain.sample.application.dto.response.get_sample_response import (
    GetSampleResponseDto,
)


class SampleService:
    def __init__(self):
        pass

    async def get_sample(self, sample_id: int) -> GetSampleResponseDto:
        return GetSampleResponseDto(id=sample_id, name="Sample", description="Sample description")
