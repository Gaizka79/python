### Users DB API ###

from fastapi import APIRouter, HTTPException, status
from db.models.user import User
from db.schemas.user import user_schema, users_schema
#from db.mongo_config import db_client
from db.client import db_client
from bson import ObjectId

router = APIRouter(prefix="/userdb",
                    tags=["userdb"],
                    responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})

users_list = []

@router.get("/")#, response_model=list[User])
async def users():
    return users_schema(db_client.users.find())

@router.get("/{id}")  #Path --> http://localhost:8000/userdb/1
async def user_id(id: str):
    return search_user("_id", ObjectId(id))
    
@router.get("/")      #Query --> http://localhost:8000/userdb/?id=1
async def user(id: str):
    return search_user("_id", ObjectId(id))

@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def post_user(user: User):
    print(User)
    if type(search_user("email", user.email)) == User:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="El usuario ya existe")

    user_dict = dict(user)
    del user_dict["id"]
    id = db_client.users.insert_one(user_dict).inserted_id
    new_user = user_schema(db_client.users.find_one({"_id": id}))

    return User(**new_user)

@router.put("/", response_model=User)
async def edit_user(user: User):
    
    user_dict = dict(user)
    del user_dict["id"]
    
    try:
        db_client.users.find_one_and_replace(
            {"_id": ObjectId(user.id)}, user_dict)
    except:
        raise HTTPException(status_code=404, detail="No se ha encontrado el usuario")
        

    return search_user("_id", ObjectId(user.id))

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(id: str):
    
    found = db_client.users.find_one_and_delete({"_id": ObjectId(id)})
    if not found:
        raise HTTPException(status_code=404, detail="No se ha encontrado el usuario")
        #return {"error": "No se ha eliminado el usuario"}

    return {"message": "Usuario eliminado correctamente"}
    

def search_user(field: str, key):
    try:
        user = db_client.users.find_one({field: key})
        print(user_schema(user))
        return User(**user_schema(user))
      
    except:
        return {"error": "No se ha encontrado el usuario"}

def search_user_by_email(email: str):
    try:
        user = db_client.users.find_one({"email": email})
        return User(**user_schema(user))
    except:
        return {"error": "No se ha encontrado el usuario"}