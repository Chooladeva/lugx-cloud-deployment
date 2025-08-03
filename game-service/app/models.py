from sqlalchemy import Column, Integer, String, Float, Date
from .database import Base

class Game(Base):
    __tablename__ = "games"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    release_date = Column(Date, nullable=True)
    price = Column(Float, nullable=False)
