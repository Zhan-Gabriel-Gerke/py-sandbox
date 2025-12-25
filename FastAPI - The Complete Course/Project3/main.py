from fastapi import FastAPI
from .routes import auth, todos, admin, users

from .models import Base
from .database import engine
#uvicorn main:app --reload
#uvicorn Project3.main:app --reload
app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/healthy")
def get_healthy():
    return {"status": "healthy"}


app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(users.router)
