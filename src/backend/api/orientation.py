from fastapi import APIRouter, Query
from .model import DataSchema, DataDB
from crud import crud
from datetime import datetime

router = APIRouter()

@router.post("/orientation/", response_model=DataDB, status_code=201)
async def create_data(payload: DataSchema):
    data = await crud.create_data(payload)
    return data

@router.get("/orientation/{id}", response_model=DataDB, status_code=200)
async def get_one_data(id: int):
    data = await crud.get_one_data(id)
    return data

@router.get("/orientation/", response_model=list[DataDB], status_code=200)
async def get_all_data(start_date: datetime | None = Query(None),
                       end_date: datetime | None = Query(None)):
    data = await crud.get_all_data(start_date, end_date)
    return data

@router.get("/orientation/grouped/", response_model=dict, status_code=200)
async def get_all_grouped_data(steps: int):
    data = await crud.get_all_grouped_data(steps)
    return data


@router.put("/orientation/{id}", response_model=DataDB, status_code=200)
async def update_data(id: int, payload: DataSchema):
    data = await crud.update_data(id, payload)
    return data

@router.delete("/orientation/{id}", response_model=DataDB, status_code=200)
async def delete_data(id: int):
    data = await crud.delete_data(id)
    return data
