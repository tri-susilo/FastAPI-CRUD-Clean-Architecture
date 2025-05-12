from typing import Optional
from sqlmodel import SQLModel
from datetime import datetime

class UserCreate(SQLModel):
    name : str
    email : str

class UserRead(SQLModel):
    id : int
    name : str
    email : str
    is_active : bool
    created_at : datetime

class UserUpdate(SQLModel):
    name : Optional[str] = None 
    email : Optional[str] = None
    is_active : Optional[bool] = None
    
