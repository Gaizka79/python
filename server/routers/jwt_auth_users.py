import os
from dotenv import load_dotenv

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta

load_dotenv()
ALGORITHM=os.getenv('ALGORITHM')
ACCESS_TOKEN_EXPIRES =os.getenv('ACCESS_TOKEN_EXPIRES')
SECRET = os.getenv('SECRET')

router = APIRouter()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

crypt = CryptContext(schemes=["bcrypt"])


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
        "password": "$2a$12$rblNkTFhdoyPA.b/C6AlAeo8tpqy4WV3.Asc54FKhoo0UJNxQ3qPi"  #123456
    },
    "Adele": {
        "username": "Adele",
        "full_name": "Adele Arrondo",
        "email": "Adele@mail.com",
        "disabled": False,
        "password": "$2a$12$E/WBrN8AFR0iq1fEAPKhqeuWLRNBXuCNB.aKwcM3ra894OpsoQv6e"  #654321
    }
}

def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])

def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])

async def auth_user(token: str = Depends(oauth2)):

    exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="El token no es correcto",
            headers={"WWW-Authenticate": "Bearer"})
    try:
        username = jwt.decode(token, SECRET, algorithms=[ALGORITHM]).get("sub")
        if username is None:
            raise exception

    except JWTError:
        raise exception

    return search_user(username)

        


async def current_user(user: User = Depends(auth_user)):
    if user.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Usuario inactivo")
    return user


@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="El usuario no es correcto")

    user = search_user_db(form.username)
    #print(user)
    
    if not crypt.verify(form.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="El contrase??a no es correcta")

    access_token = {
        "sub": user.username, 
        "exp": datetime.utcnow() + timedelta(minutes=int(ACCESS_TOKEN_EXPIRES))
    }

    return {
        "access_token": jwt.encode(access_token, SECRET, algorithm=ALGORITHM), 
        "token_type": "bearer"}


@router.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user

