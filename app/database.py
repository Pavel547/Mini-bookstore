from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import os
from dotenv import load_dotenv

load_dotenv()

POOSTGRE_SQL_URL = os.getenv("DB_URL")

engine = create_engine(POOSTGRE_SQL_URL)

SessionLocall = sessionmaker(bind=engine, autoflush=False, autocommit = False)

Base = declarative_base()
