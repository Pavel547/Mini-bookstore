from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.database import SessionLocall, engine

models.Base.metadata.create_all(bind=engine)

mini_lib = FastAPI()

def get_db():
    db = SessionLocall()
    try:
       yield db
    finally:
        db.close
        
@mini_lib.post("/create_writer/", response_model=schemas.WriterCreate)
def add_writer(writer: schemas.WriterCreate, db: Session = Depends(get_db)):
    create_writer = crud.get_writer_by_name(db=db, writer_name=writer.name)
    if create_writer is None:
        raise HTTPException(status_code=400, detail="Writer already exists")
    return crud.create_writer(db=db, writer=writer)

@mini_lib.get("/get_writer/name/{writer_name}", response_model=schemas.Writer)
def get_writer_by_name(name: str, db: Session = Depends(get_db)):
    get_writer = crud.get_writer_by_name(db=db, writer_name=name)
    if get_writer is None:
        raise HTTPException(status_code=400, detaili="Writer not found")
    return get_writer

@mini_lib.get("/get_writer/id/{writer_id}", response_model=schemas.Writer)
def get_writer_by_id(writer_id: int, db: Session = Depends(get_db)):
    get_writer = crud.get_writer_by_id(db=db, id=writer_id)
    if get_writer is None:
        raise HTTPException(status_code=404, detail="Writer not found")
    return get_writer

@mini_lib.get("/get_writer/pseudonym/{writer_pseudonym}", response_model=schemas.Writer)
def get_writer_by_pseudonym(writer_pseudonym: str, db: Session = Depends(get_db)):
    get_writer = crud.get_writer_by_pseudonym(db=db, pseudo=writer_pseudonym)
    if get_writer is None:
        raise HTTPException(status_code=404, detail="Writer not found")
    return get_writer

@mini_lib.get("/get_writers/", response_model=schemas.Writer)
def get_writers(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    get_writers = crud.get_writers(db=db, skip=skip, limit=limit)
    return get_writers

