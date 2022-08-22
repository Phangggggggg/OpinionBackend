from fastapi import APIRouter
import pymongo
import datetime
import numpy as np
from bson.json_util import dumps

from bson.json_util import loads
import json
from ..config.database_connection import database

router = APIRouter(
    prefix="/articles",
    tags=["articles"],
    responses={404: {"description": "Not found"}},
)

collection = database.test_news

# class New(BaseModel):
# 	title: str
# 	article: str
# 	description: str
# 	date: str
# 	link: str
# 	xclass: int
# 	image: str




@router.put("/retrieve")
async def retrieveNews():
	news = list(collection.find())
	red_news= list(collection.find({'perdicted_class': '2'}))
	yellow_news = list(collection.find({'perdicted_class': '1'}))
	neutral_news = list(collection.find({'perdicted_class': '0'}))
	focused_keys=["_id","title","description","link","xclass","perdicted_class","img","date","percent"]
	resp={}
 	
     
	lst_json = []
	red_json = []
	yellow_json = []
	neutral_json = [] 
	for new in news:
		doc_resp={}
		for key in focused_keys:
			if key=="_id":
				doc_resp["id"]=str(new[key])
			else:
				doc_resp[key]=new[key]
		lst_json.append(doc_resp)
	resp["test_news"] = lst_json;
 
	for new in yellow_news:
		doc_resp={}
		for key in focused_keys:
			if key=="_id":
				doc_resp["id"]=str(new[key])
			else:
				doc_resp[key]=new[key]
		yellow_json.append(doc_resp)
	resp["yellow_news"] = yellow_json;
	
	for new in neutral_news:
		doc_resp={}
		for key in focused_keys:
			if key=="_id":
				doc_resp["id"]=str(new[key])
			else:
				doc_resp[key]=new[key]
		neutral_json.append(doc_resp)
	resp["neutral_news"] = neutral_json;
 
	for new in red_news:
		doc_resp={}
		for key in focused_keys:
			if key=="_id":
				doc_resp["id"]=str(new[key])
			else:
				doc_resp[key]=new[key]
		red_json.append(doc_resp)
	resp["red_news"] = red_json;
	
	return resp

