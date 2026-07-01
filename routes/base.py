from fastapi import APIRouter
import os

# APIrouter is a class that allows the route seperation across files(modules).
base_router = APIRouter(
    # prefix means adding a keyword before every route below
    # ex. the "/" route , afer the prefix below it can only accessed by /api/v2 then /
    prefix="/api/v",
    #tags for mark every group of routes with specific tag
    tags = ["base"]
)

@base_router.get("/")
async def wel():
# async is used in function definition to apply asynchronous interaction 
    # we()
    name = os.getenv("APP_NAME")
    return {
        "message":name
    }
