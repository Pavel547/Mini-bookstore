from sqlalchemy.orm import Session

from app import models, schemas

def add_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(
        title = book.title,
        description = book.description,
        author = book.author,
        genre = book.genre,
        price = book.price,
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def get_book_by_id(db: Session, id: int):
    return db.query(models.Book).filter(models.Book.id==id).first()

def get_book_by_title(db: Session, title: str):
    return db.query(models.Book).filter(models.Book.title==title).first()

def get_book_by_ganre(db: Session, genre: str):
    return db.query(models.Book).filter(models.Book.genre==genre).all()
