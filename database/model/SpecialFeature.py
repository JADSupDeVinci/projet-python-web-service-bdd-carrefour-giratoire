from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, Session
from database.Engine import Engine
from database.model.AbstractEntity import AbstractEntity

class SpecialFeature(AbstractEntity):
    __tablename__ = 'view_special_features'
    id: Mapped[str] = mapped_column(primary_key=True)
    feature_name: Mapped[str] = mapped_column(String(50))

    @property
    def SpecialFeatureId(self):
        return self.id

    @property
    def SpecialFeatureName(self):
        return self.feature_name

    @classmethod
    def get_all_special_features(cls):
        with Session(Engine.getEngine()) as session:
            return session.query(cls).all()

    def __repr__(self):
        return f"Special Feature Id: {self.id}, Special Feature Name: {self.feature_name}"

    def toDict(self):
        return {
            'Special Feature Id': self.id,
            'Special Feature Name': self.feature_name
        }