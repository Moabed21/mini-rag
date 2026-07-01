from fastapi import FastAPI
from routes import base # Import the module itself
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

app.include_router(base.base_router)