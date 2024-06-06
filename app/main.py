# from typing import Optional, List
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# from fastapi.params import Body
# from pydantic import BaseModel

# from random import randrange
# import psycopg2
# from psycopg2.extras import RealDictCursor
# import time
# from sqlalchemy.orm import Session
from . import database,schemas, model
# import .model
# import schemas
# import util
# #from .database import engine, SessionLocal
# import database
from .routers import post, user, auth, vote
from .config import settings




# database.Base.metadata.create_all(bind = database.engine)



origins = ["*"]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# while True:
#     try:
#         conn = psycopg2.connect(host = 'localhost', database = 'fastapi', user = 'postgres', password = 'password1234', cursor_factory= RealDictCursor)
#         cursor = conn.cursor()
#         print("database connection was success")
#         break
#     except Exception as error:
#         print("connecting to database failed")
#         print("error: ", error)
#         time.sleep(2)


# my_posts = [{"title": "title of post1", "content": "content of post1","id": 1},
#             {"title": "favorite foods", "content": "i like pizza", "id":2}]


# def find_post(id):
#     for p in my_posts:
#         if p["id"] == id:
#             return p
        
# def find_index_post(id):
#     for i,p in enumerate(my_posts):
#         if p['id'] == id:
#             return i


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message": "hello world"}







