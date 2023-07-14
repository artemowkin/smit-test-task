from fastapi import FastAPI

from .settings import settings
from .db import init_db, shutdown_db
from .api.v1.routes import router as router_v1
from .api.v1.commands import init_insurances


app = FastAPI(
    docs_url='/api/docs/' if settings.mode == 'development' else None,
    redoc_url='/api/docs/' if settings.mode == 'development' else None,
    openapi_url='/api/openapi.json' if settings.mode == 'development' else None,
    title='SMIT Test Task',
)


app.include_router(router_v1, prefix='/api/v1', tags=['insurances'])


@app.on_event('startup')
async def on_startup():
    await init_db()
    await init_insurances()


@app.on_event('shutdown')
async def on_shutdown():
    await shutdown_db()
