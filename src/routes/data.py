from fastapi import APIRouter, Depends, UploadFile
from helpers.config import get_settings, Settings
from controllers import DataController

data_router = APIRouter(
    prefix="/api/v1/data",
    tags= ["/api/v1/","data"]
)

@data_router.post("/upload/{project_id}")
async def upload_data(project_id : str,file: UploadFile,
    app_settings : Settings = Depends(get_settings)):
    # paremeters are: input file,path parameter, env vars

    # because the validation is logic work we seperate it
    # in controllers then call it here
    is_valid = DataController().validate_uploaded_file(file=file)

    return is_valid