from pydantic import BaseModel
from typing import List, Dict
from datetime import datetime

class OrderCreate(BaseModel):
    customer_name: str
    items: List[Dict[str, int]]  # list of {"game_id": int, "quantity": int}
    total_price: float

class Order(OrderCreate):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
