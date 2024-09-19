from datetime import datetime
from typing import Tuple

from pydantic import BaseModel, PositiveInt, EmailStr

class Delivery(BaseModel):
    timestamp: datetime
    dimensions: Tuple[int, int]

class UserCreate(BaseModel):
    name: str
    email : EmailStr

class UserCreated(UserCreate):
    id: int


