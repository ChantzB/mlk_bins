#!/usr/bin/env python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

base = declarative_base()
base_copy = 1

class Record(base):
    __tablename__ = "record"

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    title = Column('title', String)
    artist = Column('artist', String)
    year = Column('year', String)
    rec_company = Column('rec_company', String)
    producer = Column('producer', String)
    copies = Column('copies', Integer)

    def __init__(self, title, artist, year, rec_company, producer, copies):
        self.title = title
        self.artist = artist
        self.year = year
        self.rec_company = rec_company
        self.producer = producer
        self.copies = base_copy

    def add_copy(self):
        self.copy = self.copy + 1

