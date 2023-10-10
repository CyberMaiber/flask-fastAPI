from fastapi import APIRouter, HTTPException
from db import database, goods 
from typing import List
from models import GoodsOne, GoodsIn

router = APIRouter()

@router.get("/goods/", response_model=List[GoodsOne])
async def read_goods():
    query = goods.select()
    return await database.fetch_all(query)


@router.post("/goods/", response_model=GoodsOne)
async def create_good(good: GoodsIn):
    query = goods.insert().values(**good.dict())
    last_record_id = await database.execute(query)
    return {**good.dict(), "id": last_record_id}


@router.get("/goods/{good_id}", response_model=GoodsOne)
async def read_good(good_id: int):
    query = goods.select().where(goods.c.id == good_id)
    return await database.fetch_one(query)


@router.put("/goods/{good_id}", response_model=GoodsIn)
async def update_good(good_id: int, new_good: GoodsIn):
    query = goods.update().where(goods.c.id == good_id).values(**new_good.dict())
    await database.execute(query)
    return {**new_good.dict(), "id": good_id}


@router.delete("/goods/{good_id}")
async def delete_good(good_id: int):
    query = goods.delete().where(goods.c.id == good_id)
    await database.execute(query)
    return {'message': 'Good one deleted'}