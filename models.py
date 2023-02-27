from sqlalchemy import Column, create_engine, Table, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import INTEGER, String
from scrapy.utils.project import get_project_settings

Base = declarative_base()


def db_connect():
    return create_engine(get_project_settings().get("CONNECTION_STRING"))


def create_table(engine):
    try:
        Base.metadata.create_all(engine)
        print("Table Created")
    except:
        print("Error while creating table")


class Quote(Base):
    __tablename__ = "Quote"
    id = Column(INTEGER, primary_key=True)
    Quote = Column('Quote', String)
    Author = Column('AUthor', String)
    Tags = Column('Tags', String)