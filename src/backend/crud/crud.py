from api.model import CompassSchema, RawDataSchema
from db.session import session
from db.model import Compass, RawData
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError

async def create_data(payload: CompassSchema):
    try:
        data = Compass(
            angle=payload.angle
        )
        session.add(data)
        session.commit()
        return data
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=409, detail=f"Error while creating data: {e}")

async def get_one_data(id: int):
    data = session.query(Compass).filter(Compass.id == id).first()
    if data is None:
        raise HTTPException(status_code=404, detail="Data not found")
    return data

async def get_all_data():
    data = session.query(Compass).all()
    return data

async def update_data(id: int, payload: CompassSchema):
    try:
        data: Compass = await get_one_data(id)
        data.angle = payload.angle
        session.add(data)
        session.commit()
        return data
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=409, detail=f"Error while updating data: {e}")

async def delete_data(id: int):
    data: Compass = await get_one_data(id)
    session.delete(data)
    session.commit()
    return data

async def create_raw_data(id: int, payload: RawDataSchema):
    try:
        data = RawData(
            value=payload.value,
        )
        session.add(data)
        session.commit()
        return data
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=409, detail=f"Error while creating raw data: {e}")

async def get_one_raw_data(id: int):
    data = session.query(RawData).filter(RawData.id == id).first()
    if data is None:
        raise HTTPException(status_code=404, detail="Raw data not found")
    return data

async def get_all_raw_data():
    data = session.query(RawData).all()
    return data

async def update_raw_data(id: int, payload: RawDataSchema):
    try:
        data: RawData = await get_one_raw_data(id)
        data.value = payload.value
        session.add(data)
        session.commit()
        return data
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=409, detail=f"Error while updating raw data: {e}")
    
async def delete_raw_data(id: int):
    data: RawData = await get_one_raw_data(id)
    session.delete(data)
    session.commit()
    return data
