from fastapi import APIRouter, HTTPException
from db import database, customers 
from typing import List
from models import Customer, CustomerIn

router = APIRouter()

@router.get("/")
async def home():
    return {"Home": "Home"}


@router.get("/customers/", response_model=List[Customer])
async def read_customers():
    query = customers.select()
    return await database.fetch_all(query)


@router.post("/customers/", response_model=Customer)
async def create_customer(customer: CustomerIn):
    query = customers.insert().values(**customer.dict())
    last_record_id = await database.execute(query)
    return {**customer.dict(), "id": last_record_id}


@router.get("/customers/{customer_id}", response_model=Customer)
async def read_customer(customer_id: int):
    query = customers.select().where(customers.c.id == customer_id)
    return await database.fetch_one(query)


@router.put("/customers/{customer_id}", response_model=CustomerIn)
async def update_customer(customer_id: int, new_customer: CustomerIn):
    query = customers.update().where(customers.c.id == customer_id).values(**new_customer.dict())
    await database.execute(query)
    return {**new_customer.dict(), "id": customer_id}


@router.delete("/customers/{customer_id}")
async def delete_customer(customer_id: int):
    query = customers.delete().where(customers.c.id == customer_id)
    await database.execute(query)
    return {'message': 'Customer deleted'}