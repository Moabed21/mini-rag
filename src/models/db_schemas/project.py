from pydantic import BaseModel, Field, field_validator, ConfigDict
from typing import Optional
from bson.objectid import ObjectId

class Project(BaseModel):
    # any document inserted in mongodb automatically an _id attribute is added to it
    _id: Optional[ObjectId]

    # project id minimum attributes 
    project_id: str = Field(..., min_length=1)

    # a custom validation method
    @field_validator('project_id')
    def validate_project_id(cls, value):
        if not value.isalnum():
            raise ValueError('project_id must be alphanumeric')
        return value
    
    model_config=ConfigDict(arbitrary_types_allowed=True)
        # this tells pydantic: if you find an unknown type like objectid skip it