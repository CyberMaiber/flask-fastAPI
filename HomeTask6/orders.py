from fastapi import APIRouter, HTTPException
from db import database, orders 
from typing import List
from models import OrdersOne, OrdersIn

router = APIRouter()

@router.get("/orders/", response_model=List[OrdersOne])
async def read_orders():
    query = orders.select()
    return await database.fetch_all(query)


@router.post("/orders/", response_model=OrdersIn)
async def create_order(order: OrdersIn):
    query = orders.insert().values(**order.dict())
    last_record_id = await database.execute(query)
    return {**order.dict(), "id": last_record_id}


@router.get("/orders/{order_id}", response_model=OrdersOne)
async def read_order(order_id: int):
    query = orders.select().where(orders.c.id == order_id)
    return await database.fetch_one(query)


@router.put("/orders/{order_id}", response_model=OrdersIn)
async def update_order(order_id: int, new_order: OrdersIn):
    query = orders.update().where(orders.c.id == order_id).values(**new_order.dict())
    await database.execute(query)
    return {**new_order.dict(), "id": order_id}


@router.delete("/orders/{order_id}")
async def delete_order(order_id: int):
    query = orders.delete().where(orders.c.id == order_id)
    await database.execute(query)
    return {'message': 'Order one deleted'}