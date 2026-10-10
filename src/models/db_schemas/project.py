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

    model_config = ConfigDict(arbitrary_types_allowed=True)
        # this tells pydantic: if you find an unknown type like objectid skip it


    @classmethod
    def get_indexes(cls):
        # this is a static function used to be accessed using a class instance 
        # for this reason we named cls instead of self 
        return [
            {
                # here we are searching with only one field (project_id), we put it in the "key"
                # number 1 means we are searching ascending, -1 for descending.
                "key": [
                    ("project_id", 1)
                ],
                # put a unique name 
                "name": "project_id_index_1",
                # means all values in this field must be unique if set to True, else raise an error
                "unique": True

            }
        ]
        #returns a list of all indicies i want to apply