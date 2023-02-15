from typing import Type

import pytest

from pymongo.collection import Collection

from config import Database, load_config
from models.dao import UserDataAccessObject


class TestDao:
    @pytest.fixture()
    def dao(self):
        test_collection: Collection = load_config().db.db["UserTest"]
        UserDataAccessObject.collection = test_collection
        return UserDataAccessObject

    # def test_create(self, dao: Type[UserDataAccessObject]):
    #     user = dao.create(id=1, sex="male")
    #     assert user.id == 1
    #     assert user.sex == "male"

    def test_get(self, dao: Type[UserDataAccessObject]):
        # user = dao.create(id=1, sex="male")
        user2 = dao.get(id=1)
        assert user2.id == 1
