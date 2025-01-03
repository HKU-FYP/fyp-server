from fastapi import APIRouter, Depends, status

router = APIRouter(tags=["Sample"])

@router.get("/simple-sample", status_code=status.HTTP_200_OK)
async def get_samples():
    return {"message": "Hello, World!"}