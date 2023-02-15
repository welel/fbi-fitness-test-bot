import pytest
from pydantic import ValidationError
from pymongo.collection import Collection

from config import Database, load_config
from errors import errors
from models.dao import UserDataAccessObject
from models.models import TestResult, User


class TestModel:
    def test_test_result_default(self):
        test_result: TestResult = TestResult()
        assert test_result.situps == 0
        assert test_result.sprint == 0
        assert test_result.pushups == 0
        assert test_result.running == 0
        assert test_result.pullups == 0

    def test_test_result_less_than_zero(self):
        with pytest.raises(ValidationError):
            TestResult(situps=-1)
        with pytest.raises(ValidationError):
            TestResult(sprint=-1)
        with pytest.raises(ValidationError):
            TestResult(pushups=-1)
        with pytest.raises(ValidationError):
            TestResult(running=-1)
        with pytest.raises(ValidationError):
            TestResult(pullups=-1)

    def test_user(self):
        user = User(id=1, sex="male")
        assert user.id == 1
        assert user.sex == "male"

    def test_user_id_less_than_zero(self):
        with pytest.raises(ValidationError):
            User(id=-1, sex="male")

    def test_user_sex(self):
        with pytest.raises(ValidationError):
            User(id=1, sex="x")

    def test_user_results(self):
        result = TestResult()
        user = User(id=1, sex="male", results=[result])
        assert user.results == [result]
        with pytest.raises(ValidationError):
            User(results=["result"])


class TestDao:
    @pytest.fixture()
    def dao(self):
        db: Database = load_config().db
        test_collection: Collection = db.db["UserTest"]
        UserDataAccessObject.collection = test_collection

        yield

        UserDataAccessObject.collection.delete_many({})
        db.client.close()

    def test_create(self, dao):
        user = UserDataAccessObject.create(id=1, sex="male")
        assert user.id == 1
        assert user.sex == "male"

    def test_create_with_results(self, dao):
        result_1 = TestResult()
        result_2 = TestResult(sprint=20)
        results = [result_1, result_2]
        user = UserDataAccessObject.create(id=1, sex="male", results=results)
        assert user.id == 1
        assert user.results[0] == result_1
        assert user.results[1] == result_2
        assert user.results[1].sprint == 20

    def test_create_already_exists(self, dao):
        UserDataAccessObject.create(id=1, sex="male")
        with pytest.raises(errors.UserAlreadyExists):
            UserDataAccessObject.create(id=1, sex="male")

    def test_create_validation(self, dao):
        with pytest.raises(ValidationError):
            UserDataAccessObject.create(id=-1, sex="male")
        with pytest.raises(ValidationError):
            UserDataAccessObject.create(id=1, sex="x")

    def test_get(self, dao):
        user = UserDataAccessObject.create(id=1, sex="male")
        gotten_user = UserDataAccessObject.get(id=1)
        assert user.id == gotten_user.id

    def test_get_user_does_not_exists(self, dao):
        with pytest.raises(errors.UserDoesNotExists):
            UserDataAccessObject.get(id=1)

    def test_get_validation(self, dao):
        with pytest.raises(ValueError):
            UserDataAccessObject.get(id="str")

    def test_update(self, dao):
        user = UserDataAccessObject.create(id=1, sex="male")
        user.sex = "female"
        UserDataAccessObject.update(user)
        updated_user = UserDataAccessObject.get(id=1)
        assert updated_user.sex == "female"

    def test_update_user_does_not_exists(self, dao):
        user = User(id=1, sex="male")
        user.sex = "female"
        with pytest.raises(errors.UserDoesNotExists):
            UserDataAccessObject.update(user)
