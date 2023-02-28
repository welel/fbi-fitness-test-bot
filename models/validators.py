import re
from math import ceil

from pydantic import ValidationError

from lexicon.lexicon_en import LEXICON_EN

from .models import TestResult, Repetition, Second, Millisecond


def validate_repetitions(repetition: Repetition | str) -> Repetition | str:
    # `situps` same as `pushups` and `pullups`
    try:
        result = TestResult.validate({"situps": repetition})
    except ValidationError:
        return LEXICON_EN["repetition_not_integer"]
    return result.situps


def validate_seconds(time: str) -> Second | str:
    # format 01:23 (min:sec)
    if re.fullmatch(r"\d\d\:\d\d", time):
        minutes, seconds = [int(value) for value in time.split(":")]
        if (minutes >= 60 or minutes < 0) or (seconds >= 60 or seconds < 0):
            return LEXICON_EN["wrong_seconds_format"]
        return minutes * 60 + seconds
    else:
        return LEXICON_EN["wrong_seconds_format"]


def validate_milliseconds(time: str) -> Millisecond | str:
    # format 1.23 (sec:ms)
    time = time.strip()
    if re.fullmatch(r"\d+\.\d+", time):
        result = ceil(float(time) * 1000)
        return result if result >= 0 else 0
    else:
        return LEXICON_EN["wrong_milliseconds_format"]
