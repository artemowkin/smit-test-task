import json

from app.settings import INIT_JSON_FILE
from .models import Insurance


async def init_insurances():
    """This command initiates insurances from init json file"""
    if await Insurance.all().count():
        return

    with INIT_JSON_FILE.open() as f:
        init_json = json.load(f)

    for date in init_json:
        for insurance in init_json[date]:
            await Insurance.create(**insurance, date=date)
