from pydantic import BaseModel, Field, validator
from typing import Optional
from bson.objectid import ObjectId

class Project(BaseModel):
    # any document inserted in mongodb automatically an _id attribute is added to it
    _id: Optional[ObjectId]

    # project id minimum attributes 
    project_id: str = Field(..., min_length=1)

    @validator('project_id')
    def validate_peoject_id(cls, value):
        if not value.isalnum():
            raise ValueError('project_id must be alphanumeric')
        return value
    
    class Config:
        arbitrary_types_allowed = True
        # this tells pydantic: if you find an unknown type like objectid skip it