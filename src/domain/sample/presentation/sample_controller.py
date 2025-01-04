from fastapi import APIRouter, Depends, status

from src.domain.di_container import sample_service
from src.domain.sample.application.dto.response.get_sample_response import (
    GetSampleResponseDto,
)

router = APIRouter(tags=["Sample"])


@router.get(
    "/samples/{sample_id}",
    status_code=status.HTTP_200_OK,
    response_model=GetSampleResponseDto,
)
async def get_samples(sample_id: int):
    return await sample_service.get_sample(sample_id)
