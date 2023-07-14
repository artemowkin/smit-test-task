from decimal import Decimal

from .models import Insurance
from .schemas import CalculateRequest
from .utils import handle_doesnt_exist


@handle_doesnt_exist('There is no insurance with cargo type `{0.cargo_type.value}` for date `{0.date}`')
async def calculate_insurance(data: CalculateRequest) -> Decimal:
    """Calculates declared value with ensurance rate"""
    insurance = await Insurance.get(date=data.date, cargo_type=data.cargo_type.value)
    return data.declared_value * insurance.rate
