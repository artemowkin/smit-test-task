from tortoise import Tortoise

from app.settings import settings


async def init_db():
    await Tortoise.init(db_url=settings.database_url, modules={
        'models': ['app.api.v1.models']
    })
    await Tortoise.generate_schemas()


async def shutdown_db():
    await Tortoise.close_connections()
