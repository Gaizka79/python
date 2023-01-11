# users.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class User(BaseModel):
    id: int
    name: str
    surname: str
    email: str
    age: int

users_list = [User(id=1,name="Gaizka", surname="Arrondo", email="gaizka@mail.com", age=44),
                User(id=2,name="Ira", surname="Agiriano", email="Ira@mail.com", age=39),
                User(id=3,name="Adele", surname="Arrondo", email="Adele@mail.com", age=6),
                User(id=4,name="Ager", surname="Arrondo", email="Ager@mail.com", age=3)]

@router.get("/usersjson")
async def userjson():
    return [{"id": 1, "name": "Gaizka", "surname": "Arrondo", "email": "gaizka@mail.com", "age": 44},
            {"id": 2, "name": "Ira", "surname": "Agiriano", "email": "ira@mail.com", "age": 39},
            {"id": 3, "name": "Adele", "surname": "Arrondo", "email": "adele@mail.com", "age": 6},
            {"id": 4, "name": "Ager", "surname": "Arrondo", "email": "ager@mail.com", "age": 3}]

@router.get("/users")
async def users():
    return users_list

@router.get("/user/{id}")  #Path --> http://localhost:8000/user/1
async def user_id(id: int):
    return search_user(id)
    
@router.get("/user/")      #Query --> http://localhost:8000/user/?id=1
async def user(id: int):
    return search_user(id)

@router.post("/user/", status_code=201)
async def post_user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=404, detail="El usuario, ya existe")
    users_list.append(user)
    return user

@router.put("/user/")
async def put_user(user: User):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
        
    if not found:
        raise HTTPException(status_code=404, detail="No se ha encontrado el usuario")

    return user

@router.delete("/user/{id}")
async def delete_user(id: int):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True
        
    if not found:
        return {"error": "No se ha encontrado el usuario"}

    return {"message": "Usuario eliminado correctamente"}
    

     




def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
      return list(users)[0]
    except:
      return {"error": "No se ha encontrado el usuario"}

    