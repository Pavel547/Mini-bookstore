from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship

from app.database import Base

class Writer(Base):
    __tablename__ = "writers"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    pseudonym = Column(String, index=True)
    
    books_written = ForeignKey("Book", back_populates="author")
    
    
class Book(Base):
    __tablename__ = "books"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    genre = Column(String)
    in_lib = Column(Boolean)
    writer_name = relationship("writers.name")
    
    author = ForeignKey("Writer", back_populates="books_written")

