from datetime import datetime
from enum import Enum

from pydantic import BaseModel, validator, ValidationError
from pydantic.fields import Field

from errors.errors import CalculationError
from lexicon.lexicon_en import LEXICON_EN

from .calculation_data import TEST_TABLE


Repetition = int
Second = int
Millisecond = int


class Exercise(str, Enum):
    SITUPS = "situps"
    SPRINT = "sprint"
    PUSHUPS = "pushups"
    RUNNING = "running"
    PULLUPS = "pullups"


class Sex(str, Enum):
    MALE = "male"
    FEMALE = "female"


class TestResult(BaseModel):
    created: datetime = Field(default_factory=datetime.now)
    situps: Repetition = Field(default=0, ge=0)
    sprint: Millisecond = Field(default=0, ge=0)
    pushups: Repetition = Field(default=0, ge=0)
    running: Second = Field(default=0, ge=0)
    pullups: Repetition = Field(default=0, ge=0)
    score: int = Field(default=0, ge=0)

    @staticmethod
    def _get_score(
        value: Repetition | Second | Millisecond, sex: Sex, exercise: Exercise
    ) -> int:
        intervals = TEST_TABLE[sex][exercise]
        for interval, score in intervals.items():
            start, end = interval
            if start <= value <= end:
                return score
        else:
            raise CalculationError

    def calculate(self, sex: Sex):
        score = TestResult._get_score(self.situps, sex, Exercise.SITUPS)
        score += TestResult._get_score(self.pushups, sex, Exercise.PUSHUPS)
        score += TestResult._get_score(
            self.pullups, Sex.MALE, Exercise.PULLUPS
        )
        score += TestResult._get_score(self.sprint, sex, Exercise.SPRINT)
        score += TestResult._get_score(self.running, sex, Exercise.RUNNING)
        self.score = score

    def __str__(self) -> str:
        result = self.dict().copy()
        result["sprint"] = "{} sec {} ms".format(
            result["sprint"] // 1000, result["sprint"] % 1000
        )
        result["running"] = "{} min {} sec".format(
            result["running"] // 60, result["running"] % 60
        )
        return LEXICON_EN["test_result"].format(**result)


class User(BaseModel):
    id: int = Field(ge=0)
    sex: Sex
    results: list[TestResult] = Field(default_factory=list)

    @validator("sex")
    def validate_sex(cls, sex: str) -> str:
        if sex not in ("male", "female"):
            raise ValidationError("Sex should be male or female.")
        return sex
