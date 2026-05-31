"""
Day 70 Milestone Project: Build a RESTful Task/Todo API 🚀
----------------------------------------------------------
Combine HTTP routing, status codes, Pydantic schemas, and FastAPI endpoints 
by engineering a RESTful Task/Todo API.

Task Requirements:
1. Define a Pydantic schema 'TodoItem' containing:
   - title (str)
   - description (str, optional)
   - completed (bool, default False)
2. Define a list database locally to hold records.
3. Construct FastAPI endpoints:
   - GET `/todos`: Fetch all todos.
   - POST `/todos`: Create a new todo item (returns 201 Created).
   - PUT `/todos/{todo_id}`: Update completed status.
   - DELETE `/todos/{todo_id}`: Remove item.
4. Run using `uvicorn day_70_todo_api:app --reload` and test via http://127.0.0.1:8000/docs
"""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="Todo API Manager")

class TodoItem(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

# Local memory database mock
todos_db = {}
id_counter = 1

@app.get("/todos", response_model=List[dict])
def get_all_todos():
    # TODO: Return all items in todos_db
    return []

@app.post("/todos", status_code=status.HTTP_201_CREATED)
def create_todo(item: TodoItem):
    global id_counter
    # TODO: Insert new item into todos_db with key id_counter and increment
    return {"message": "Todo created successfully"}

@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, completed: bool):
    # TODO: Fetch item from todos_db, update completed status, or raise 404 error
    return {"message": "Updated"}

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    # TODO: Delete item from todos_db or raise 404 error
    return {"message": "Deleted"}
