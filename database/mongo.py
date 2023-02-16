from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database as MongoDatabase

from config import MongoDB, load_config


class Database:
    config: MongoDB = load_config().mongo_db

    @classmethod
    def get_client(cls) -> MongoClient:
        return MongoClient(cls.config.connection_string)

    @classmethod
    def get_database(cls) -> MongoDatabase:
        client = cls.get_client()
        return client[cls.config.name]

    @classmethod
    def get_collection(cls, name: str | None = None) -> Collection:
        database = cls.get_database()
        return database[cls.config.collection_name if not name else name]
