from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from flask import Flask

Base = declarative_base()
engine = create_engine("mysql+mysqldb://localhost:3306/pillbox")

class Pill(Base):
    __tablename__ = "pillbox_master"

    id = Column(Integer, primary_key=True)


app = Flask(__name__)

@app.route("/")
def index():
    return "Hello there..."

if __name__ == "__main__":
    app.run()