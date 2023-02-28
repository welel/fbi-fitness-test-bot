from models.validators import (
    validate_milliseconds,
    validate_seconds,
    validate_repetitions,
)
from lexicon.lexicon_en import LEXICON_EN


def test_milliseconds_validator_invalid_values():
    assert validate_milliseconds("") == LEXICON_EN["wrong_milliseconds_format"]
    assert (
        validate_milliseconds("1.") == LEXICON_EN["wrong_milliseconds_format"]
    )
    assert (
        validate_milliseconds(".1") == LEXICON_EN["wrong_milliseconds_format"]
    )
    assert (
        validate_milliseconds("11") == LEXICON_EN["wrong_milliseconds_format"]
    )


def test_milliseconds_validator_valid_values():
    assert validate_milliseconds("0.0") == 0
    assert validate_milliseconds("0.1") == 100
    assert validate_milliseconds("0.12") == 120
    assert validate_milliseconds("0.123") == 123
    assert validate_milliseconds("0.1234") == 124
    assert validate_milliseconds("0.12345") == 124
    assert validate_milliseconds("1.0") == 1000
    assert validate_milliseconds("1.1") == 1100
    assert validate_milliseconds("10.1") == 10100
    assert validate_milliseconds("10.01") == 10010


def test_seconds_validator_invalid_values():
    assert validate_seconds("") == LEXICON_EN["wrong_seconds_format"]
    assert validate_seconds("0") == LEXICON_EN["wrong_seconds_format"]
    assert validate_seconds("0:0") == LEXICON_EN["wrong_seconds_format"]
    assert validate_seconds("12:") == LEXICON_EN["wrong_seconds_format"]
    assert validate_seconds(":12") == LEXICON_EN["wrong_seconds_format"]
    assert validate_seconds("1:23") == LEXICON_EN["wrong_seconds_format"]
    assert validate_seconds("12:1") == LEXICON_EN["wrong_seconds_format"]
    assert validate_seconds("123:12") == LEXICON_EN["wrong_seconds_format"]
    assert validate_seconds("12:123") == LEXICON_EN["wrong_seconds_format"]
    assert validate_seconds("01:70") == LEXICON_EN["wrong_seconds_format"]
    assert validate_seconds("70:59") == LEXICON_EN["wrong_seconds_format"]


def test_seconds_validator_valid_values():
    assert validate_seconds("00:00") == 0
    assert validate_seconds("00:01") == 1
    assert validate_seconds("00:10") == 10
    assert validate_seconds("00:59") == 59
    assert validate_seconds("01:00") == 60
    assert validate_seconds("01:01") == 61
    assert validate_seconds("10:05") == 605


def test_repetition_validator_invalid_values():
    assert validate_repetitions(-1) == LEXICON_EN["repetition_not_integer"]
    assert validate_repetitions("-1") == LEXICON_EN["repetition_not_integer"]
    assert validate_repetitions("1.7") == LEXICON_EN["repetition_not_integer"]


def test_repetition_validator_valid_values():
    assert validate_repetitions(0) == 0
    assert validate_repetitions(1) == 1
    assert validate_repetitions(1.2) == 1
    assert validate_repetitions(1.5) == 1
    assert validate_repetitions(1.7) == 1
    assert validate_repetitions(10) == 10
    assert validate_repetitions(100) == 100
