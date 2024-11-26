from pydantic import BaseModel
from datetime import datetime
from fastapi import HTTPException

class DataSchema(BaseModel):
    angle: float

class DataDB(DataSchema):
    id: int
    timestamp: datetime = datetime.now()



class RawDataSchema(BaseModel):
    value: float

class RawDataDB(RawDataSchema):
    id: int
    timestamp: datetime = datetime.now()