from fastapi import FastAPI
from routes import auth, todos


import models
from database import engine
#uvicorn main:app --reload

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(todos.router)

