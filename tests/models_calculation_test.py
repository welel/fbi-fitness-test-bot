from models.models import TestResult, Sex, Exercise
from models.validators import validate_seconds, validate_milliseconds


def test_get_score_situps_male():
    assert TestResult._get_score(0, Sex.MALE, Exercise.SITUPS) == -2
    assert TestResult._get_score(31, Sex.MALE, Exercise.SITUPS) == -2
    assert TestResult._get_score(32, Sex.MALE, Exercise.SITUPS) == 0
    assert TestResult._get_score(38, Sex.MALE, Exercise.SITUPS) == 1
    assert TestResult._get_score(39, Sex.MALE, Exercise.SITUPS) == 2
    assert TestResult._get_score(44, Sex.MALE, Exercise.SITUPS) == 3
    assert TestResult._get_score(46, Sex.MALE, Exercise.SITUPS) == 4
    assert TestResult._get_score(58, Sex.MALE, Exercise.SITUPS) == 10
    assert TestResult._get_score(1000, Sex.MALE, Exercise.SITUPS) == 10


def test_get_score_pushups_male():
    assert TestResult._get_score(0, Sex.MALE, Exercise.PUSHUPS) == -2
    assert TestResult._get_score(1, Sex.MALE, Exercise.PUSHUPS) == -2
    assert TestResult._get_score(19, Sex.MALE, Exercise.PUSHUPS) == -2
    assert TestResult._get_score(20, Sex.MALE, Exercise.PUSHUPS) == 0
    assert TestResult._get_score(31, Sex.MALE, Exercise.PUSHUPS) == 1
    assert TestResult._get_score(39, Sex.MALE, Exercise.PUSHUPS) == 2
    assert TestResult._get_score(45, Sex.MALE, Exercise.PUSHUPS) == 4
    assert TestResult._get_score(71, Sex.MALE, Exercise.PUSHUPS) == 10
    assert TestResult._get_score(1000, Sex.MALE, Exercise.PUSHUPS) == 10


def test_get_score_pullups_male():
    assert TestResult._get_score(0, Sex.MALE, Exercise.PULLUPS) == 0
    assert TestResult._get_score(1, Sex.MALE, Exercise.PULLUPS) == 0
    assert TestResult._get_score(2, Sex.MALE, Exercise.PULLUPS) == 1
    assert TestResult._get_score(5, Sex.MALE, Exercise.PULLUPS) == 2
    assert TestResult._get_score(15, Sex.MALE, Exercise.PULLUPS) == 7
    assert TestResult._get_score(20, Sex.MALE, Exercise.PULLUPS) == 10
    assert TestResult._get_score(1000, Sex.MALE, Exercise.PULLUPS) == 10


def test_get_score_sprint_male():
    result = validate_milliseconds("00.00")
    assert TestResult._get_score(result, Sex.MALE, Exercise.SPRINT) == 10
    result = validate_milliseconds("55.1")
    assert TestResult._get_score(result, Sex.MALE, Exercise.SPRINT) == -2
    result = validate_milliseconds("55.0")
    assert TestResult._get_score(result, Sex.MALE, Exercise.SPRINT) == 0
    result = validate_milliseconds("51.1")
    assert TestResult._get_score(result, Sex.MALE, Exercise.SPRINT) == 1
    result = validate_milliseconds("45.5")
    assert TestResult._get_score(result, Sex.MALE, Exercise.SPRINT) == 5
    result = validate_milliseconds("40.9")
    assert TestResult._get_score(result, Sex.MALE, Exercise.SPRINT) == 10


def test_get_score_running_male():
    result = validate_seconds("00:00")
    assert TestResult._get_score(result, Sex.MALE, Exercise.RUNNING) == 10
    result = validate_seconds("00:01")
    assert TestResult._get_score(result, Sex.MALE, Exercise.RUNNING) == 10
    result = validate_seconds("13:30")
    assert TestResult._get_score(result, Sex.MALE, Exercise.RUNNING) == -2
    result = validate_seconds("13:29")
    assert TestResult._get_score(result, Sex.MALE, Exercise.RUNNING) == 0
    result = validate_seconds("12:15")
    assert TestResult._get_score(result, Sex.MALE, Exercise.RUNNING) == 1
    result = validate_seconds("11:40")
    assert TestResult._get_score(result, Sex.MALE, Exercise.RUNNING) == 2
    result = validate_seconds("09:00")
    assert TestResult._get_score(result, Sex.MALE, Exercise.RUNNING) == 9
    result = validate_seconds("08:59")
    assert TestResult._get_score(result, Sex.MALE, Exercise.RUNNING) == 10
