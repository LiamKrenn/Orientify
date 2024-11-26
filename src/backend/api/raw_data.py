from fastapi import APIRouter
from .model import RawDataSchema, RawDataDB
from crud import crud

router = APIRouter()

@router.post("/raw_data/", response_model=RawDataDB, status_code=201)
async def create_raw_data(payload: RawDataSchema):
    data = await crud.create_data(payload)
    return data

@router.get("/raw_data/{id}", response_model=RawDataDB, status_code=200)
async def get_one_raw_data(id: int):
    data = await crud.get_one_data(id)
    return data

@router.get("/raw_data/", response_model=list[RawDataDB], status_code=200)
async def get_all_raw_data():
    data = await crud.get_all_data()
    return data

@router.put("/raw_data/{id}", response_model=RawDataDB, status_code=200)
async def update_raw_data(id: int, payload: RawDataSchema):
    data = await crud.update_data(id, payload)
    return data

@router.delete("/raw_data/{id}", response_model=RawDataDB, status_code=200)
async def delete_raw_data(id: int):
    data = await crud.delete_data(id)
    return data

