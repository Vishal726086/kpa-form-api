from sqlalchemy import Column, Integer, String
from app.database import Base

class FormData(Base):
    __tablename__ = "form_data"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    district = Column(String, nullable=True)
    block = Column(String, nullable=True)
    village = Column(String, nullable=True)
    address = Column(String, nullable=True)
    category = Column(String, nullable=True)
    sub_category = Column(String, nullable=True)
    occupation = Column(String, nullable=True)
    organization = Column(String, nullable=True)
