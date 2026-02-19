from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Foto(Base):
    __tablename__ = "fotos"

    id = Column(Integer, primary_key=True)
    name_foto = Column(String)
    path = Column(Integer)