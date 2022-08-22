from fastapi import APIRouter
import pymongo
import datetime

from bson.json_util import dumps

import json
from ..config.database_connection import database

router = APIRouter(
    prefix="/opinion",
    tags=["opinion"],
    responses={404: {"description": "Not found"}},
)
collection = database.test_opinions

@router.put("/retrieve")
async def retrieveOpinionNews():
    news_opinion=list(collection.find())
    focused_opinions_keys=["_id","title","description","link","img","date"]
    resp={}
    opinion_json = []
    for new in news_opinion:
        doc_resp={}
        for key in focused_opinions_keys:
            if key=="_id":
                doc_resp["id"]=str(new[key])
            else:
                doc_resp[key]=new[key]
        opinion_json.append(doc_resp)
    resp["test_opinion"] = opinion_json
    return resp
    
