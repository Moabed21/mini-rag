from enum import Enum

class ResponseSignal(Enum):
    FILE_NOT_SUPPORTED = "Not supported types!"
    FILE_SIZE_EXCEEDED = "Above the allowed size!"
    FILE_SUCCESSFULLY_VALIDATED = "Successfully Validated!"
    FILE_UPLOAD_SUCCEED = "file_upload_succeed"
    FILE_UPLOAD_SUCCESS = "file_upload_succeed"
    FILE_UPLOAD_FAILED = "file_upload_failed"
    PROCESSING_SUCCEED = "Processing Succeed!"
    PROCESSING_SUCCESS = "Processing Succeed!"
    PROCESSING_FAILED = "Processing Failed!"
    FILE_ID_ERROR = "File id not found!"
    NO_FILES_ERROR = "No files found for this project!"
