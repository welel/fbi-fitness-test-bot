from typing import Literal

from pymongo.collection import Collection

from database.mongo import Database
from errors.errors import UserAlreadyExists, UserDoesNotExists
from .models import User, TestResult


class UserDataAccessObject:
    collection: Collection = Database.get_collection()

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
        result = cls.collection.update_one(
            {"id": user.id}, {"$set": user.dict()}
        )
        if not result.matched_count:
            raise UserDoesNotExists(user.id)
        return user

    @classmethod
    def get(cls, id: int) -> User:
        if not isinstance(id, int):
            raise ValueError
        user_data = cls.collection.find_one({"id": id})
        if not user_data:
            raise UserDoesNotExists(id=id)
        return User(**user_data)
