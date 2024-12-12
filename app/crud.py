from sqlalchemy.orm import Session
from sqlalchemy import asc, desc

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
    return db.query(models.Book).filter(models.Book.id == id).first()

def get_book_by_title(db: Session, title: str):
    return db.query(models.Book).filter(models.Book.title == title).first()

def get_book_by_ganre(db: Session, genre: str):
    return db.query(models.Book).filter(models.Book.genre == genre).all()

def get_books_above_price(db: Session, price: float):
    return db.query(models.Book).filter(models.Book.price > price).all()

def get_books_cheaper_price(db: Session, price: float):
    return db.query(models.Book).filter(models.Book.price < price).all()

def get_books_by_price(order: str, db: Session):
    if order == "asc":
        return db.query(models.Book).order_by(asc(models.Book.price)).all()
    else:
        return db.query(models.Book).order_by(desc(models.Book.price)).all()
    
def update_book_info_numerosity(db: Session, book_title: str, update_data: schemas.BookUpdate):
    books = db.query(models.Book).filter(models.Book.title == book_title).first()
    books.numerosity = update_data
    db.commit()
    db.refresh(books)
    return books

def update_book_info_instock(db: Session, book_title: str, update_data: schemas.BookUpdate):
    books = db.query(models.Book).filter(models.Book.title == book_title).first()
    books.in_stock = update_data
    db.commit()
    db.refresh(books)
    return books


def dell_book(db: Session, book: schemas.Book):
    db.delete(book)
    db.commit()
