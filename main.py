# uvicorn main:app --reload

import uvicorn
from fastapi import FastAPI
from server.routers import products, users, basic_auth_users, jwt_auth_users, users_db
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

if __name__ == "__main__":
  uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

app = FastAPI()

# Middleware
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Routers
app.include_router(products.router)
app.include_router(users.router)
app.include_router(basic_auth_users.router)
app.include_router(jwt_auth_users.router)
app.include_router(users_db.router)
app.mount("/static", StaticFiles(directory="./server/static"), name="static")

@app.get("/")
async def root():
    return {"Kaixo": "World"}

@app.get("/kaixo/")
async def kaixo():
    return {"message":"Kaixo munduari!"}
