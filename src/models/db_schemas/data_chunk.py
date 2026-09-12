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
