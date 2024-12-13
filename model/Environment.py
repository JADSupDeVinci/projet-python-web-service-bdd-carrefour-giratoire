from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, Session
from database.Engine import Engine
from database.model.AbstractEntity import AbstractEntity

class Environment(AbstractEntity):
    __tablename__ = 'view_environment'
    id: Mapped[str] = mapped_column(primary_key=True)
    environment_name: Mapped[str] = mapped_column(String(50))

    @property
    def EnvironmentId(self):
        return self.id

    @property
    def EnvironmentName(self):
        return self.environment_name

    @classmethod
    def get_all_environments(cls):
        with Session(Engine.getEngine()) as session:
            return session.query(cls).all()

    def __repr__(self):
        return f"Environment Id: {self.id}, Environment Name: {self.environment_name}"

    def toDict(self):
        return {
            'Environment Id': self.id,
            'Environment Name': self.environment_name
        }