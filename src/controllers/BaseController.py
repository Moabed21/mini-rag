from fastapi import Depends
from helpers.config import get_settings

class BaseController:

    def __init__(self):
        self.app_settings = Depends(get_settings)