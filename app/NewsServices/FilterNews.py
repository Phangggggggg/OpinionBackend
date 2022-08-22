from cgitb import lookup
from threading import local
from fastapi import APIRouter
from pydantic import BaseModel

from ..config.database_connection import database

router = APIRouter(
    prefix="/filter",
    tags=["filter"],
    responses={404: {"description": "Not found"}},
)

collection=database.test_votes
collection_opinion=database.test_opinion

class User(BaseModel):
	user_id: str


@router.put("/filternews")
async def filterNews(user: User):
    if collection.count_documents({"user_id":user.user_id})==0:
        return {"status":"No filter news"}
    else:
        cursor=list(collection.find({"user_id": user.user_id}, {"news_id": 1,"xclass":1,"_id":0}))
        return {"status":"Success","news_ids":cursor}
		
