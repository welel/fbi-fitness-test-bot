from datetime import datetime

from pydantic import BaseModel, validator, ValidationError
from pydantic.fields import Field


class TestResult(BaseModel):
    created: datetime = Field(default_factory=datetime.now)
    situps: int = Field(default=0, ge=0)
    sprint: int = Field(default=0, ge=0)
    pushups: int = Field(default=0, ge=0)
    running: int = Field(default=0, ge=0)
    pullups: int = Field(default=0, ge=0)
    score: int = Field(default=0, ge=0)


class User(BaseModel):
    id: int = Field(ge=0)
    sex: str
    results: list[TestResult] = Field(default_factory=list)

    @validator("sex")
    def validate_sex(cls, sex: str) -> str:
        if sex not in ("male", "female"):
            raise ValidationError("Sex should be male or female.")
        return sex
