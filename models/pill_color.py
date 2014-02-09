from sqlalchemy import Column, Integer, String
from db import Base, session

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