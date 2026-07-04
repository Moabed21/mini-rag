from fastapi import APIRouter, Depends, UploadFile, status, HTTPException
from controllers import DataController, ProjectController
from helpers.config import get_settings, Settings
from fastapi.responses import JSONResponse
from models.enums import ResponseSignal
import aiofiles
import logging
import os

logger = logging.getLogger('server.error')

data_router = APIRouter(
	prefix="/api/v1/data",
	tags= ["/api/v1/","data"]
)

@data_router.post("/upload/{project_id}")
async def upload_data(project_id : str,file: UploadFile,
	app_settings : Settings = Depends(get_settings)):
	# paremeters are: input file, path parameter, env vars

	# because the validation is logic work we seperate it
	# in controllers then call it here
	is_valid, result = DataController().validate_uploaded_file(file=file)

	if not is_valid:
		raise HTTPException(
			status_code=status.HTTP_400_BAD_REQUEST,
			detail=result
		)

	project_dir_path = ProjectController().get_project_path(project_id)
	# now we got the full file directory path
	 
	file_path= DataController().generate_unique_filename(
		ori_filename=file.filename,
		project_id=project_id
	)
	# now we got the path of the file itself

	# ---------------file storing operation---------------------------------
	try:
		async with aiofiles.open(file_path,"wb") as f:
			# wb means open any file in writemode as binary 
			while chunk := await file.read(app_settings.FILE_DEFAULT_CHUNK_SIZE):
				await f.write(chunk)
	# ----------------------------------------------------------------------
	except Exception as e:
		logger.error(f"error while uploading the file {e}")
		JSONResponse(
		content={"signal": ResponseSignal.FILE_UPLOAD_FAILED.value},
		status_code=status.HTTP_200_OK
	)
	return JSONResponse(
		content={"signal": ResponseSignal.FILE_SUCCESSFULLY_VALIDATED.value},
		status_code=status.HTTP_200_OK
	)