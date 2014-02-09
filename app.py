from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from flask import Flask

Base = declarative_base()
engine = create_engine("mysql+mysqldb://root@localhost:3306/pillbox")
session = sessionmaker(bind=engine)()

class PillColor(Base):
    __tablename__ = "SPL_color_lookup"

    color_number = Column(Integer, primary_key=True)
    color = Column(String)
    SPL_code = Column(String)
    hex_value = Column(String)

    @classmethod
    def generate_pill_color_code_map(self):
        pill_colors = session.query(PillColor).order_by(PillColor.color_number)
        color_map = {}

        for pill_color in pill_colors:
            color_map[pill_color.SPL_code] = pill_color.color

        return color_map


class PillShape(Base):
    __tablename__ = "SPL_shape_lookup"

    shape_number = Column(Integer, primary_key=True)
    shape_type = Column(String)
    SPL_code = Column(String)

    def type(self):
        return self.shape_type

    @classmethod
    def generate_pill_shape_code_map(self):
        pill_shapes = session.query(PillShape).order_by(PillShape.shape_number)
        shape_map = {}

        for pill_shape in pill_shapes:
            shape_map[pill_shape.SPL_code] = pill_shape.shape_type

        return shape_map


class Pill(Base):
    __tablename__ = "pillbox_master"

    id = Column(Integer, primary_key=True)
    MEDICINE_NAME = Column(String)
    SPLSHAPE = Column(String)
    SPLCOLOR = Column(String)
    PILL_COLORS = PillColor.generate_pill_color_code_map()
    PILL_SHAPES = PillShape.generate_pill_shape_code_map()

    def __repr__(self):
        return "<Pill Shape: %s Color: %s Name: %s>" % \
            (self.colors(), self.shape(), self.name())

    def colors(self):
        try:
            return [self.PILL_COLORS[x] for x in self.SPLCOLOR.split(";")]
        except KeyError:
            # Lots of dirty data (iee SPLCOLOR;SPLCOLOR,SPLCOLOR;;,;;SPLCOLOR)
            return [""]

    def name(self):
        return self.MEDICINE_NAME

    def shape(self):
        try:
            return self.PILL_SHAPES[self.SPLSHAPE]
        except KeyError:
            return ""

app = Flask(__name__)
@app.route("/")
def index():
    return "Hello there..."

if __name__ == "__main__":
    app.run()