from sqlalchemy.orm import Session

from app import models, schemas

def create_writer(db: Session, writer: schemas.WriterCreate):
    create_writer_in_db = models.Writer(name=writer.name, pseudonym=writer.pseudonym)
    db.add(create_writer_in_db)
    db.commit()
    db.refresh(create_writer_in_db)
    return create_writer_in_db

def get_writer_by_name(db: Session, writer_name: str):
    return db.query(models.Writer).filter(models.Writer.name==writer_name).first()

def get_writer_by_id(db: Session, writer_id: int):
    return db.query(models.Writer).filter(models.Writer.id==writer_id).first()

def get_writer_by_pseudonym(db: Session, writer_pseudo: str):
    return db.query(models.Writer).filter(models.Writer.pseudonym==writer_pseudo).first()

def get_writers(db: Session, skip: int = 0, limit: int = 20):
    return db.query(models.Writer).offset(skip).limit(limit).all()

def get_items(db: Session, skip: int = 0, limit: int = 20):
    return db.query(models.Book).offset(skip).limit(limit).all()

def create_book(db: Session, book: schemas.BookCreate, author_name: str):
    create_book_in_db = models.Book(
        name=book.name,
        description=book.description,
        genre=book.genre,
        in_lib=book.in_lib,
        writer_name=author_name
    )
    db.add(create_book_in_db)
    db.commit()
    db.refresh(create_book_in_db)
    return create_book_in_db

def get_book_by_id(db: Session, id: int):
    return db.query(models.Book).filter(models.Book.id==id).first()

def get_book_by_name(db: Session, name: str):
    return db.query(models.Book).filter(models.Book.name==name).first()

def get_book_by_author(db: Session, author_name: str):
    return db.query(models.Book).filter(models.Book.author==author_name).first()

def get_books(db: Session, skip: int = 0, limit: int = 20):
    return db.query(models.Book).offset(skip).limit(limit).all()
