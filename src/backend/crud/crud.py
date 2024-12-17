from api.model import DataSchema, RawDataSchema
from db.session import session
from db.model import Data, RawData
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.sql import func
from datetime import datetime

async def create_data(payload: DataSchema):
    try:
        if payload.angle > 360:
            raise ValueError("Winkel muss zwischen 0 und 360 liegen.")
        data = Data(
            angle=payload.angle
        )
        session.add(data)
        session.commit()
        return data
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=409, detail=f"Error while creating data: {e}")

async def get_one_data(id: int):
    data = session.query(Data).filter(Data.id == id).first()
    if data is None:
        raise HTTPException(status_code=404, detail="Data not found")
    return data

async def get_all_data(start_date: datetime | None = None, end_date: datetime | None = None):
    query = session.query(Data)

    if start_date:
        query = query.filter(Data.timestamp >= start_date)
    if end_date:
        query = query.filter(Data.timestamp <= end_date)

    data = query.all()
    return data

async def get_all_grouped_data(steps: int):
    if steps <= 0 or steps > 360:
        raise HTTPException(status_code=409, detail=f"Steps müssen zwischen 1 und 360 liegen.")

    query = session.query(Data.angle, func.count(Data.id)).group_by(Data.angle)
    results = query.all()

    grouped_data = {}
    for i in range(0, 360, steps):
        range_start = i
        range_end = i + steps - 1
        
        if range_end > 360:
            range_end = 359

        total_count = 0
        for row in results:
            angle = round(row[0])
            count = row[1] 
            if range_start <= angle <= range_end:
                total_count += count
        
        grouped_data[f"{range_start}-{range_end}"] = total_count

    return grouped_data


async def update_data(id: int, payload: DataSchema):
    try:
        data: Data = await get_one_data(id)
        data.angle = payload.angle
        session.add(data)
        session.commit()
        return data
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=409, detail=f"Error while updating data: {e}")

async def delete_data(id: int):
    data: Data = await get_one_data(id)
    session.delete(data)
    session.commit()
    return data

async def create_raw_data(payload: RawDataSchema):
    try:
        data = RawData(
            microphone1Data=payload.microphone1Data,
            microphone2Data=payload.microphone2Data,
            timeDifference=payload.timeDifference,
            microphonesDistance=payload.microphonesDistance,
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
        data.microphone1Data = payload.microphone1Data
        data.microphone2Data = payload.microphone2Data
        data.timeDifference = payload.timeDifference
        data.microphonesDistance = payload.microphonesDistance
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
