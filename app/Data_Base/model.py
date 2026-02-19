from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class Foto(Base):
    __tablename__ = "fotos"

    id = Column(Integer, primary_key=True)
    name_foto = Column(String(255), nullable=False)
    path = Column(String(512), nullable=False)

    def __repr__(self):
        return f"<Foto(id={self.id}, name_foto='{self.name_foto}', path='{self.path}')>"