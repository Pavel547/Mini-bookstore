from pydantic import BaseModel

class BookBase(BaseModel):
    name: str
    description: str
    genre: str
    in_lib: bool
    writer_name: str
    
class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int
    
    class Confige:
        from_attributes = True
        
class WriterBase(BaseModel):
    name: str
    pseudonym: str

class WriterCreate(WriterBase):
    pass

class Writer(WriterBase):
    id: int
    books_written: list[Book] = []
    
    class Config:
        from_attributes = True
 