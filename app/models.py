from sqlalchemy import Column, Integer, String, Boolean, Float
from app.database import Base

class Book(Base):
    __tablename__ ="books"
    
    id = Column(Integer, index=True, primary_key=True)
    title = Column(String, index=True)
    description = Column(String, nullable=True)
    author = Column(String, index=True)
    genre = Column(String)
    price = Column(Float, index=True)
    in_stock = Column(Boolean, index=True, default=False)
    numerosity = Column(Integer)
