from fastapi import APIRouter
import pymongo
from pydantic import BaseModel

from ..config.database_connection import database

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={404: {"description": "Not found"}},
)

collection=database.test_user

class User(BaseModel):
	username: str
	password: str

@router.put("/")
async def validator(user: User):
	if collection.count_documents({"username":user.username})==0:
		return {"status":"Username doesn't exist"}
	else:
		cursor=collection.find({"username":user.username})
		password=cursor[0]["password"]
		name=cursor[0]["name"]
		fullname=cursor[0]['fullname']
		birthday=cursor[0]['birthday']
		phone=cursor[0]['phone']
		user_id = str(cursor[0]['_id'])
		if user.password==password:
			return {"status":"pass","user":{
				"id": user_id,
				"email": name,
				"username":user.username,
				"fullname":fullname,
				"birthday":birthday,
				"phone":phone,
			}}
		else:
			return {"status":"fail"}
