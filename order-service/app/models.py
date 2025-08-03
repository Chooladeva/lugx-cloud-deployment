from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.dialects.postgresql import JSON
from datetime import datetime
from .database import Base

class Order(Base):
    __tablename__ = "orders"
    
    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String, nullable=False)
    items = Column(JSON, nullable=False)  # list of {game_id, quantity}
    total_price = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
