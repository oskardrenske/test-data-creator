import os
import random
import time
import pathlib
from datetime import datetime, timedelta
import json

from loguru import logger

from src import settings


def create_dir(dir_name: str) -> pathlib.Path:
    p = pathlib.Path(dir_name)
    p.mkdir(parents=True, exist_ok=True)
    return p


def create_phone_number() -> str:
    """
    returns a random string of numbers between 0100000000 and 0999999999
    """
    rnd = random.randint(100000000, 999999999)
    return f"0{rnd}"


def random_true_false() -> bool:
    """
    Returns True or False randomly
    """
    return random.choice([True, False])


def street_number():
    """
    returns a string of digits from 1 to 128
    """
    return str(random.randint(1, 128))


def get_random_from_list(list_of_things):
    return random.sample(list_of_things, k=1)[0]


def timestamp():
    """
    returns current time and date in a formatted string
    """
    return time.strftime(settings.DATE_FORMAT, time.localtime())


def old_date() -> str:
    """
    Returns a formatted timestamp string with a date 1-500 weeks in the past
    """
    now = datetime.now()
    old = now - timedelta(weeks=random.randint(1, 500))
    return old.strftime(settings.DATE_FORMAT)


def check_if_string(var_to_check):
    if not isinstance(var_to_check, str):
        raise ValueError(f"Wrong data type: {type(var_to_check)} ")


def pretty_print(person: dict):
    """
    Prints formatted json to stdout
    """
    if settings.PRINT:
        print(json.dumps(person, indent=4, ensure_ascii=False))


def combine_prefix_suffix(prefixes: list, suffixes: list) -> list:
    combinations = []
    for pre in prefixes:
        check_if_string(pre)
        for suff in suffixes:
            check_if_string(suff)
            value = f"{pre.strip()}{suff.strip()}"
            combinations.append(value.capitalize())
    return combinations


def load_data_from_file(filename: str) -> list:
    logger.debug(f"Loading data from {filename}")
    data_from_file = []
    file_path = f"{settings.INDATA_DIRECTORY}/{filename}"
    with open(file_path, encoding="utf-8") as f:
        data = f.readlines()
        for line in data:
            data_from_file.append(line.strip())
    return data_from_file


def number_of_persons():
    """
    Some checks that there is a value in the environment variable and that it is a digit > 0
    If any of the checks fail, it's logged and the default value is used.
    """
    number_of_persons = os.getenv("NUMBER_OF_PERSONS")
    if number_of_persons is not None and number_of_persons.isdigit() and int(number_of_persons) > 0:
        return int(number_of_persons)
    else:
        logger.debug(
            f"env var was {number_of_persons}, using default value {settings.NUMBER_OF_PERSONS}"
        )
        return settings.DEFAULT_NUMBER_OF_PERSONS
