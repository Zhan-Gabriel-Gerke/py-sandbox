from fastapi import FastAPI
import models
from database import engine

#uvicorn main:app --reload

app = FastAPI()

models.Base.metadata.create_all(bind=engine)