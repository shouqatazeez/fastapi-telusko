from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


db_url = "postgresql://postgres:shouqat_7@localhost:5432/fastapi_db"
engine =  create_engine(db_url)
Session = sessionmaker(autocommit = False, autoflush=False, bind=engine)