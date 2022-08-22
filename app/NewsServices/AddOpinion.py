from hashlib import new
from fastapi import APIRouter
import pymongo
from pydantic import BaseModel

from ..config.database_connection import database

router = APIRouter(
    prefix="/news",
    tags=["news"],
    responses={404: {"description": "Not found"}},
)

collection=database.test_votes

class News(BaseModel):
	user_id: str
	news_id: str
	xclass: str


@router.put("/addopinion")
async def addOpinion(news: News):
	news_doc={"user_id": news.user_id,"news_id": news.news_id,"xclass":news.xclass}
	collection.insert_one(news_doc)
	return {"status":"add opinion success"}
   