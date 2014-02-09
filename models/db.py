from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine("mysql+mysqldb://root@localhost:3306/pillbox")
session = sessionmaker(bind=engine)()
