from fastapi import FastAPI, Request, status
from .routes import auth, todos, admin, users

from .models import Base
from .database import engine
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from fastapi.responses import RedirectResponse


# uvicorn main:app --reload
# uvicorn Project3.main:app --reload
app = FastAPI()

Base.metadata.create_all(bind=engine)

# Строим абсолютный путь от текущего файла
BASE_DIR = Path(__file__).resolve().parent

app.mount("/static", StaticFiles(directory=str(Path(BASE_DIR, 'static'))), name="static")

@app.get("/")
def test(request: Request):
    return RedirectResponse(url="todos/todo-page", status_code=status.HTTP_302_FOUND)

@app.get("/healthy")
def get_healthy():
    return {"status": "healthy"}

app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(users.router)
