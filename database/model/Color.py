from sqlalchemy import String, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, Session
from database.Engine import Engine
from database.model.AbstractEntity import AbstractEntity

class Color(AbstractEntity):
    __tablename__ = 'view_colors'
    id: Mapped[str] = mapped_column(Integer, primary_key=True, autoincrement=True)
    color_name: Mapped[str] = mapped_column(String(50))

    @property
    def ColorId(self):
        return self.id

    @property
    def ColorName(self):
        return self.color_name

    @classmethod
    def addColor(cls, color):
        with Session(Engine.getEngine()) as session:
            session.add(color)
            session.commit()
    @classmethod
    def deleteColor(self, color_id):
        with Session(Engine.getEngine()) as session:
            session.delete(color_id)
            session.commit()

    @classmethod
    def putColor(cls, color_id, color_name):
        with Session(Engine.getEngine()) as session:
            color = session.query(cls).filter(cls.id == color_id).first()
            color.color_name = color_name
            session.commit()

    @classmethod
    def get_all_color(cls):
        with Session(Engine.getEngine()) as session:
            return session.query(cls).all()

    def __repr__(self):
        return f"Couleur Id: {self.id}, Nom Couleur: {self.color_name}"

    def toDict(self):
        return {
            'Couleur Id': self.id,
            'Nom Couleur': self.color_name
        }

