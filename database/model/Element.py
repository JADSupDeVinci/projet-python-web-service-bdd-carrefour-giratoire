from sqlalchemy import String, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, Session
from database.Engine import Engine
from database.model.AbstractEntity import AbstractEntity

class Element(AbstractEntity):
    __tablename__ = 'view_elements'
    id: Mapped[str] = mapped_column(Integer, primary_key=True, autoincrement=True)
    element_name: Mapped[str] = mapped_column(String(50))

    @property
    def ElementId(self):
        return self.id

    @property
    def ElementName(self):
        return self.element_name

    @classmethod
    def addElement(cls, element):
        with Session(Engine.getEngine()) as session:
            session.add(element)
            session.commit()

    @classmethod
    def get_all_elements(cls):
        with Session(Engine.getEngine()) as session:
            return session.query(cls).all()

    def __repr__(self):
        return f"Element Id: {self.id}, Element Name: {self.element_name}"

    def toDict(self):
        return {
            'Element Id': self.id,
            'Element Name': self.element_name
        }