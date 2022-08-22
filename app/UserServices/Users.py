from fastapi import APIRouter
import pymongo
from pydantic import BaseModel

from ..config.database_connection import database

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)

collection=database.test_user

class User(BaseModel):
	name: str
	username: str
	password: str
	fullname: str
	birthday: str
	phone: str



@router.put("/add")
async def addUser(user: User):
	user_doc={"name": user.name,"username": user.username,"password":user.password,
           "fullname":user.fullname,"birthday":user.birthday,"phone":user.phone}
	if collection.count_documents({"username":user.username})==0:
		collection.insert_one(user_doc)
		return {"status":"add user success"}
	else:
		return {"status":"Username already exists"}

