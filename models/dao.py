from typing import Literal

from pymongo.collection import Collection

from config import Database, load_config
from errors.errors import UserAlreadyExists, UserDoesNotExists
from .models import User, TestResult


database: Database = load_config().db


class UserDataAccessObject:
    collection: Collection = database.db["User"]

    @classmethod
    def create(
        cls,
        id: int,
        sex: Literal["male", "female"],
        results: list[TestResult] = list(),
    ) -> User:
        if cls.collection.find_one({"id": id}):
            raise UserAlreadyExists(id)
        user = User(id=id, sex=sex, results=results)
        cls.collection.insert_one(user.dict())
        return user

    @classmethod
    def update(cls, user: User) -> User:
        cls.collection.update_one({"id": user.id}, {"$set": user.dict()})
        return user

    @classmethod
    def get(cls, id: int) -> User:
        user_data = cls.collection.find_one({"id": id})
        if not user_data:
            raise UserDoesNotExists(id=id)
        return User(**user_data)
