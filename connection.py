from sqlalchemy import create_engine
from config import sqlalchemy_database_uri

engine = create_engine(sqlalchemy_database_uri)