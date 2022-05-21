from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from os import environ as env

from dotenv import load_dotenv
load_dotenv()

db_username = env["db_username"]
db_password= env["db_password"]

SQLALCHEMY_DATABASE_URL = f"postgresql://{db_username}:{db_password}@172.20.0.1/postgres"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
