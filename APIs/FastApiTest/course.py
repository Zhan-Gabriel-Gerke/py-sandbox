import uvicorn
# if __name__ == "__main__":
#     config = uvicorn.Config("main:app", port=8000, log_level="info")
#     server = uvicorn.Server(config)
#     server.run()

from fastapi import FastAPI
from pydantic import BaseModel

#2. Create an instance of app with FastAPI, which initializes Starlette
app = FastAPI()

#3. Define the Pydantic model for the Page object to validate its data

class Page(BaseModel):
    title: str
    content: str
    views: str

#4. Define a POST route that accepts a Page object as the request body

@app.post("/pages/")
async def create_page(page: Page):
    return {"page": page}

#uvicorn main:app --reload      # run FastAPI

#Dependency injection

from fastapi import Depends
from typing import List

#Function that simulates db

def get_db():
    db = DatabaseConnection()
    try:
        yield db
    finally:
        db.close()

class DatabaseConnection:
    def __init__(self):
        self.pages = [
            {"title": "Page 1", "content": "Content of Page 1", "views": 10},
            {"title": "Page 2", "content": "Content of Page 2", "views": 20}
        ]

    def fetch_all_pages(self):
        return self.pages

    def close(self):
        pass

@app.get("/pagesv2/", responses_model=List[Page])
async def read_pages(db: DatabaseConnection = Depends(get_db)):
    return db.fetch_all_pages()