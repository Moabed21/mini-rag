from helpers.config import get_settings
import os

class BaseController:

    def __init__(self):
        self.app_settings = get_settings()
        self.base_dir = os.path.dirname(os.path.dirname(__file__)) 
        # os.path.dirname(__file__) for .../src/controllers/   (1 level up)
        # self.base_dir = os.path.dirname(os.path.dirname(__file__)) .../src/    (2 levels up) = base_dir
        self.files_dir = os.path.join(
            self.base_dir,
            "assets/files"
        )
        # → .../src/assets/files = file_dir