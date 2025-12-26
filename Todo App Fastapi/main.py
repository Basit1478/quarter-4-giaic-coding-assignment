from fastapi import FastAPI, HTTPException
from models import TodoCreate, TodoUpdate, Todo
from database import todos_db

app = FastAPI()
@app.post("/todos", response_model=Todo)
def create_todo(todo: TodoCreate):
    todo_id = len(todos_db) + 1

    new_todo = {
        "id": todo_id,
        "title": todo.title,
        "description": todo.description,
        "completed": todo.completed
    }

    todos_db.append(new_todo)
    return new_todo
@app.get("/todos", response_model=list[Todo])
def get_all_todos():
    return todos_db
@app.get("/todos/{todo_id}", response_model=Todo)
def get_todo(todo_id: int):
    for todo in todos_db:
        if todo["id"] == todo_id:
            return todo

    raise HTTPException(status_code=404, detail="Todo not found")
@app.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, updated_data: TodoUpdate):
    for todo in todos_db:
        if todo["id"] == todo_id:

            if updated_data.title is not None:
                todo["title"] = updated_data.title

            if updated_data.description is not None:
                todo["description"] = updated_data.description

            if updated_data.completed is not None:
                todo["completed"] = updated_data.completed

            return todo

    raise HTTPException(status_code=404, detail="Todo not found")
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for index, todo in enumerate(todos_db):
        if todo["id"] == todo_id:
            todos_db.pop(index)
            return {"message": "Todo deleted successfully"}

    raise HTTPException(status_code=404, detail="Todo not found")
