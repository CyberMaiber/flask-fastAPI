from pydantic import BaseModel, Field
from datetime import date
from db import customers, goods, database
# from werkzeug.security import generate_password_hash

class CustomerIn(BaseModel):
    name: str = Field(..., min_length=2, max_length=32, title="Имя покупателя") 
    email: str = Field(..., min_length=5, max_length=128, title="E-mail покупателя")
    surname: str = Field(..., min_length=2, max_length=32, title="Фамилия покупателя")
    password: str = Field(..., min_length=5, max_length=256, title="Хэш пароля покупателя")


class Customer(CustomerIn):
    id: int = Field (..., ge=1)


class GoodsIn(BaseModel):
    name: str = Field(..., min_length=2, max_length=128, title="Название товара")
    description: str = Field(..., min_length=10, max_length=1024, title="Описание товара")
    price: float = Field(..., ge=0.01,  title="Цена товара")


class GoodsOne(GoodsIn):
    id: int = Field (..., ge=1)
    

class OrdersIn(BaseModel):
    customer_id: int
    goods_id: int
    order_date: date = Field(..., format="%Y-%m-%d", title="Дата оформления заказа")
    status: str = Field(..., min_length=10, max_length=1024, title="Статус заказа")



class OrdersOne(OrdersIn):
    id: int = Field (..., ge=1)
