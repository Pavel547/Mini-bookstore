from sqlalchemy.orm import Session

from app import models, schemas

def create_writer(db: Session, writer: schemas.WriterCreate):
    create_writer = models.Writer(name=writer.name, pseudonym=writer.pseudonym)
    db.add(create_writer)
    db.commit()
    db.refresh(create_writer)
    return create_writer

def get_writer_by_name(db: Session, writer_name: str):
    return db.query(models.Writer).filter(models.Writer.name==writer_name).first()

def get_writer_by_id(db: Session, writer_id: int):
    return db.query(models.Writer).filter(models.Writer.id==writer_id).first()

def get_writer_by_pseudonym(db: Session, writer_pseudo: str):
    return db.query(models.Writer).filter(models.Writer.pseudonym==writer_pseudo).first()
