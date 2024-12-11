from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.database import SessionLocall, engine

models.Base.metadata.create_all(bind=engine)

mini_market = FastAPI()

def get_db():
    db = SessionLocall()
    try:
       yield db
    finally:
        db.close
        
@mini_market.post("/add_book/", response_model=schemas.BookCreate)
def add_book(create_book: schemas.BookCreate, db: Session = Depends(get_db)):
    get_book = crud.get_book_by_title(db=db, title=create_book.title)
    if get_book:
        raise HTTPException(status_code=400, detail="Book already exists")
    return crud.add_book(db=db, book=create_book)

@mini_market.get("/get_book/id/{book_id}", response_model=schemas.Book)
def get_book_by_id(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.get_book_by_id(db=db, id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book
    
@mini_market.get("/get_book/title/{book_title}", response_model=schemas.Book)
def get_boot_by_title(book_title: str, db: Session = Depends(get_db)):
    db_book = crud.get_book_by_title(db=db, title=book_title)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book
