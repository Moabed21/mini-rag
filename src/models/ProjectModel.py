from .BaseDataModel import BaseDataModel
from .db_schemas import Project
from .enums.DataBaseEnum import DataBaseEnum

class ProjectModel(BaseDataModel):

    def __init__(self, db_client: object):
        super().__init__(db_client)
        # we created the first collection in the DB
        self.collection = self.db_client[DataBaseEnum.COLLECTION_PROJECT_NAME.value]

    