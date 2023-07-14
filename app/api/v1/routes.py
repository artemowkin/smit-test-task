from fastapi import APIRouter

from .schemas import CalculateResponse, CalculateRequest
from .services import calculate_insurance


router = APIRouter()


@router.post('/calculate/', response_model=CalculateResponse)
async def calculate(data: CalculateRequest) -> CalculateResponse:
    """Calculates insurance value"""
    insurance_value = await calculate_insurance(data)
    return CalculateResponse(insurance_value=insurance_value)
