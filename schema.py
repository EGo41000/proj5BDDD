from datetime import datetime
from typing import Tuple

from pydantic import BaseModel, PositiveInt, EmailStr

class Delivery(BaseModel):
    timestamp: datetime
    dimensions: Tuple[int, int]

class User(BaseModel):
    id: int
    name: str = 'John Doe'
    #signup_ts: datetime
    email : EmailStr
    #tastes: dict[str, PositiveInt]


