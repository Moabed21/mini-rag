from fastapi import APIRouter, Depends, UploadFile, status, HTTPException
from fastapi.responses import JSONResponse
from helpers.config import get_settings, Settings
from controllers import DataController
from models.enums import ResponseSignal

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
    is_valid, result = DataController().validate_uploaded_file(file=file)

    if not is_valid:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=result
        )

    return JSONResponse(
        content={"signal": ResponseSignal.FILE_SUCCESSFULLY_VALIDATED.value},
        status_code=status.HTTP_200_OK
    )