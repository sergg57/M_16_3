# -*- coding: utf-8 -*-
from fastapi import FastAPI, Path

app = FastAPI()

users = {'1': 'Имя:Example, возраст: 18'}

@app.get("/users")
async def get_all_users()->dict:
    return users

# @app.get("/users/{user_id}")
# async def get_user(user_id: str)->dict:
#     return users[user_id]

@app.post("/users/{username}/{age}")
async def create_user(username: str=Path(min_length=5, max_length=20, discription='Enter username',
                example='UrbanUser'), age: int=Path(ge=18, le=120, discription='Enter age',
                example='24'))->str:
    create_user_id = str(int(max(users.keys()))+1)
    users[create_user_id] = f'Имя: {username}, возраст: {age}'
    return f"User {create_user_id} is registered"

@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: str=Path(min_length=1, max_length=10, discription='Enter user_id', example='1'), username: str=Path(min_length=5, max_length=20, discription='Enter username',
                example='UrbanUser'), age: int=Path(ge=18, le=120, discription='Enter age',
                example='24'))->str:
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f"User {user_id} has been updated"

@app.delete("/user/{user_id}")
async def delete_user(user_id: str=Path(min_length=1, max_length=10, discription='Enter user_id', example='1'))->str:
    del users[user_id]
    return f"User {user_id} has been deleted"