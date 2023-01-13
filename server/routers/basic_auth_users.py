from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import List, Dict

router = APIRouter()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool

class UserDB(User):
    password: str

users_db = {
    "Gaizka":{
        "username": "Gaizka",
        "full_name": "Gaizka Arrondo",
        "email": "gaizka@mail.com",
        "disabled": False,
        "password": "123456"
    },
    "Adele": {
        "username": "Adele",
        "full_name": "Adele Arrondo",
        "email": "Adele@mail.com",
        "disabled": False,
        "password": "654321"
    }
}

def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])

def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])

async def current_user(token: str = Depends(oauth2)):
    user = search_user(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="El token no es correcto",
            headers={"WWW-Authenticate": "Bearer"})
    if user.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Usuario inactivo")
    return user


@router.post("/loginbasic")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    print("en la funcion")
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="El usuario no es correcto")

    user = search_user_db(form.username)
    print(user)
    if not form.password == user:#.password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="El contraseña no es correcta")

    #return {"acces_token": user.username, "token_type": "bearer"}
    return {"acces_token": user, "token_type": "bearer"}

@router.get("/usersbasic/me")
async def me(user: User = Depends(current_user)):
    return user

