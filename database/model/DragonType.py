from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, Session
from database.Engine import Engine
from database.model.AbstractEntity import AbstractEntity

class DragonType(AbstractEntity):
    __tablename__ = 'view_dragon_types'
    id: Mapped[str] = mapped_column(primary_key=True)
    type_name: Mapped[str] = mapped_column(String(50))

    @property
    def DragonTypeId(self):
        return self.id

    @property
    def DragonTypeName(self):
        return self.type_name


    @classmethod
    def get_all_dragon_types(cls):
        with Session(Engine.getEngine()) as session:
            return session.query(cls).all()

    def __repr__(self):
        return f"Dragon type Id: {self.id}, Type de dragon: {self.type_name}"

    def toDict(self):
        return {
            'Dragon type Id': self.id,
            'Type de dragon': self.type_name
        }