import uvicorn
from db import database
from fastapi import FastAPI
import customers,goods,orders

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
    
app.include_router(customers.router, tags=["customers"])
app.include_router(goods.router, tags=["goods"])
app.include_router(orders.router, tags=["orders"])

if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)