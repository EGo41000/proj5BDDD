from datetime import datetime
from typing import Tuple

from pydantic import BaseModel, PositiveInt

class Delivery(BaseModel):
    timestamp: datetime
    dimensions: Tuple[int, int]
'''
'''
class User(BaseModel):
    id: int
    name: str = 'John Doe'
    signup_ts: datetime
    #tastes: dict[str, PositiveInt]

print('Schema OK')

m = Delivery(timestamp='2020-01-02T03:04:05Z', dimensions=['10', '5'])
print(repr(m))

external_data = {
    'id': 123,
    'signup_ts': '2019-06-01 12:22',
    'tastes': {
        'wine': 9,
        b'cheese': 7,
        'cabbage': '1',
    },
}

user = User(**external_data)
print('user', user)
print(user.model_dump())