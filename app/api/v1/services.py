from decimal import Decimal

from .models import Insurance
from .schemas import CalculateRequest
from .utils import handle_doesnt_exist


@handle_doesnt_exist('There is no insurance with cargo type `{0.cargo_type.value}` for date `{0.date}`')
async def calculate_insurance(data: CalculateRequest) -> Decimal:
    """Calculates declared value with ensurance rate"""
    month_str = data.date.strftime('%Y-%m')
    insurance = await Insurance.get(date__startswith=month_str, cargo_type=data.cargo_type.value)
    return data.declared_value * insurance.rate
