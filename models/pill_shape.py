from sqlalchemy import Column, Integer, String
from db import Base, session

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
