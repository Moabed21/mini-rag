from .BaseController import BaseController
from fastapi import UploadFile
from models.enums import ResponseSignal

class DataController(BaseController):
    def __init__(self):
        super().__init__()
    
    def validate_uploaded_file(self,file: UploadFile):
        
        if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES:
            return False, f"{file.content_type}: {ResponseSignal.FILE_NOT_SUPPORTED.value}"
        
        if file.size > self.app_settings.FILE_MAX_SIZE * 1048576:
            return False, f"{file.size}: {ResponseSignal.FILE_SIZE_EXCEEDED.value}"

        return True, ResponseSignal.FILE_SUCCESSFULLY_VALIDATED
