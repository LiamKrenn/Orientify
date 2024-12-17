from pydantic import BaseModel
from datetime import datetime
from fastapi import HTTPException

class DataSchema(BaseModel):
    angle: float

class DataDB(DataSchema):
    id: int
    timestamp: datetime = datetime.now()

class RawDataSchema(BaseModel):
    microphone1Data: list[int]
    microphone2Data: list[int]
    timeDifference: float
    microphonesDistance: float = 0.06

class RawDataDB(RawDataSchema):
    id: int
    timestamp: datetime = datetime.now()
