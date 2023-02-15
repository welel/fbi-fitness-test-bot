from datetime import datetime

from pydantic import BaseModel


class TestResult(BaseModel):
    datetime: datetime
    situps: int
    pushups: int
    running: int
    pullups: int
    score: int


class User(BaseModel):
    id: int
    sex: str
    results: list[TestResult]
