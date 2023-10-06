import uvicorn
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field
from typing import Annotated


app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory='static'), name='static')

class UserAttrs(BaseModel):
  name: str
  email: str

class User(UserAttrs):
  id: int = Field (ge=1)

collection = [
  User(id=1, name='Ivanov Ivan', email='ivan@ivanov.t'),
  User(id=2, name='Kuznecov Aleksey', email='aleksey@kuznecov.r'),
  User(id=3, name='Petrov Dmitriy', email='dimon@mail.ru'),
  User(id=4, name='Potapov Peter', email='peter@mail.ru'),
  User(id=5, name='Sidorov Alexander', email='alex@mail.ru')
]


@app.get('/users/', response_class=HTMLResponse)
def users(request: Request):
  return templates.TemplateResponse("users.html", {"request": request, "users": collection})

@app.get('/users/{user_id}')
def users(request: Request, user_id:int):
  for index in range(len(collection)):
    if (user_id==collection[index].id):
      return collection[index]
  return None

@app.post('/users/')
def create_users(request: Request, name: Annotated[str, Form()], email: Annotated[str, Form()]):
  user = User(collection[-1].id + 1, email=email, name=name)
  collection.append(user)
  return templates.TemplateResponse("users.html", {"request": request, "users": collection})

@app.delete('/users/{user_id}')
def delete_users(user_id:int):
  for index in range(len(collection)):
    if (user_id==collection[index].id):
      collection.pop(index)
      return True

@app.put('/users/{user_id}/{user_name}/{user_mail}')
def modify_users(user_id:int, user_name:str, user_mail:str):
  for index in range(len(collection)):
    if (user_id==collection[index].id):
      collection[index].name = user_name
      collection[index].email = user_mail
      return True


if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
