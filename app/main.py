from fastapi import FastAPI
from .UserServices import Users,Authentication
from .NewsServices import News,OpinionNews,AddOpinion,FilterNews


app = FastAPI()


app.include_router(Users.router)
app.include_router(Authentication.router)
app.include_router(News.router)
app.include_router(OpinionNews.router)
app.include_router(AddOpinion.router)
app.include_router(FilterNews.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}