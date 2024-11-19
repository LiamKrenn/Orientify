from pydantic import BaseModel
from datetime import datetime
from fastapi import HTTPException

class CompassSchema(BaseModel):
    angle: float

class CompassDB(CompassSchema):
    id: int
    timestamp: datetime = datetime.now()




