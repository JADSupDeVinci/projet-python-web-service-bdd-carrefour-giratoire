from abc import ABC

from sqlalchemy import URL, create_engine


class Engine(ABC):
    __engine = None
    @classmethod
    def getEngine(cls):
        if cls.__engine is None:
            url_object = URL.create(
                "mysql",
                username="user",
                password="user",
                host="localhost",
                database="dragon_generator"
            )
            cls.__engine = create_engine(url_object)
        return cls.__engine
