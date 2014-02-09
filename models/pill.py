from sqlalchemy import Column, Integer, String
from db import Base, session
from pill_color import PillColor
from pill_shape import PillShape

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

    @property
    def serialize(self):
        return {
            "name": self.name(),
            "colors": self.colors(),
            "shape": self.shape()
        }

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

    @classmethod
    def search_by_name(self, q):
        pills = session.query(Pill).filter(Pill.MEDICINE_NAME.like("%" + q + "%"))
        return pills.order_by(Pill.id)[0:10]