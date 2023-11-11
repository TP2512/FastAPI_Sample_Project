from fastapi import FastAPI
from database import Base, engine
import database as dtb
import models
from routers import post, user

models.db.Base.metadata.create_all(bind=dtb.engine)
app = FastAPI()
app.include_router(post.router)
app.include_router(user.router)


@app.get("/")
def root():
    return {"message": "Your at my project"}
