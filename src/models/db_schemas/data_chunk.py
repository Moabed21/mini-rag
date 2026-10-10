from pydantic import BaseModel, Field, ConfigDict
from bson.objectid import ObjectId
from typing import Optional

class DataChunk(BaseModel):
    _id: Optional[ObjectId]
    chunk_text: str = Field(..., min_length=1)
    chunk_metadata: dict
    chunk_order: int = Field(..., gt=0)
    chunk_project_id: ObjectId

    model_config=ConfigDict(arbitrary_types_allowed=True)
        # this tells pydantic: if you find an unknown type like objectid skip it

    @classmethod
    def get_indexes(cls):

        return [
            {
                "key":[
                    ("chunk_project_id", 1)
                ],
                "name": "chunk_project_id_index_1",
                # False cuz may be chunks exists with same project_id
                "unique": False
            }
        ]