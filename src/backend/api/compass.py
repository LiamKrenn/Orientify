from fastapi import APIRouter
from .model import CompassSchema, CompassDB
from crud import crud

router = APIRouter()

@router.post("/compass/", response_model=CompassDB, status_code=201)
async def create_compass(payload: CompassSchema):
    compass = await crud.create_data(payload)
    return compass

@router.get("/compass/{id}", response_model=CompassDB, status_code=200)
async def get_one_compass(id: int):
    compass = await crud.get_one_data(id)
    return compass

@router.get("/compass/", response_model=list[CompassDB], status_code=200)
async def get_all_compass():
    compass = await crud.get_all_data()
    return compass

@router.put("/compass/{id}", response_model=CompassDB, status_code=200)
async def update_compass(id: int, payload: CompassSchema):
    compass = await crud.update_data(id, payload)
    return compass

@router.delete("/compass/{id}", response_model=CompassDB, status_code=200)
async def delete_compassn(id: int):
    compass = await crud.delete_data(id)
    return compass
