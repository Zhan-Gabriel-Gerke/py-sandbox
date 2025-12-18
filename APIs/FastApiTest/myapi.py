from typing import Optional
from fastapi import FastAPI, Path
from pydantic import BaseModel

# uvicorn myapi:app --reload # run the api
# you need to be located in the folder FastApiTests
app = FastAPI()


students = {
    1: {
        "name": "John",
        "age": 17,
        "year": "year 12"
    },
    2: {
        "name": "Bose",
        "age": 99,
        "year": "year 22"
    }
}

class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[str] = None
    year: Optional[str] = None

class Student(BaseModel):
    name: str
    age: int
    year: str
@app.get("/")
def index():
    return {"name": "First Data"}

@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(description="The ID of the student you want to view", gt=0, lt=8)):
    return students[student_id]

# to a path you can pass gt, ge, le, le
# gt - Greater That
# ge - Greater that or Equal
# lt - Less That
# le - Less that or Equal

@app.get("/get-by-name/{student_id}")
def get_student(*, student_id: int, name: Optional[str] = None, test : int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data": "Not found"}

@app.post("/create-student/{student_id}")
def create_student(student_id: int, student : Student):
    if student_id in students:
        return {"Error": "Student exists"}

    students[student_id] = student
    return students[student_id]

@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"Error": "Student does not exits"}

    if student.name != None:
        students[student_id].name = student.name

    if student.age != None:
        students[student_id].age = student.age

    if student.year != None:
        students[student_id].year = student.year

    return students[student_id]

@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"Error": "Student does not exits"}

    del students[student_id]