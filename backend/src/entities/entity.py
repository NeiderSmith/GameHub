# coding=utf-8

from datetime import datetime
from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

#db_url = os.environ.get("DB_HOST") + ":" + os.environ.get("DB_PORT")
#db_name = os.environ.get("DB_NAME")
#db_user = os.environ.get("DB_USER")
#db_password = os.environ.get("DB_PASS")
#engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_url}/{db_name}')
engine = create_engine(os.getenv("DATABASE_URL"))
Session = sessionmaker(bind=engine)

Base = declarative_base()


class Entity():
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    last_updated_by = Column(String)

    def __init__(self, created_by):
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.last_updated_by = created_by
