from fastapi import FastAPI
from routes import base # Import the module itself

app = FastAPI()

app.include_router(base.base_router)