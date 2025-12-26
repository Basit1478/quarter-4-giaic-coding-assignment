from pydantic import BaseModel
from typing import Optional

# Todo create karne ke liye model
class TodoCreate(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

# Todo update karne ke liye model
class TodoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None

# Response model
class Todo(TodoCreate):
    id: int
