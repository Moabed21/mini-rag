from fastapi import FastAPI
from routes import base ,data # Import the module itself
from motor.motor_asyncio import AsyncIOMotorClient
from helpers.config import get_settings
from contextlib import asynccontextmanager
from typing import AsyncGenerator
from motor.motor_asyncio import AsyncIOMotorClient


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    settings = get_settings()
    app.mongo_conn = AsyncIOMotorClient(settings.MONGODB_URL)
    app.db_client = app.mongo_conn[settings.MONGODB_DATABASE]
    yield
    app.mongo_conn.close()

app=FastAPI(lifespan=lifespan)
    # there is plenty of events in fastapi that helps in building apps

app.include_router(base.base_router)
app.include_router(data.data_router)