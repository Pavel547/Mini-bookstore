from pydantic import BaseModel

class BookBase(BaseModel):
    title: str
    description: str | None = None
    author: str
    genre: str
    price: float
    
class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int
    in_stock: bool
    numerosity: int | None = None
 