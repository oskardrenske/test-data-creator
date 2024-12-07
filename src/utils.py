import os
import sys
import random
import time
import pathlib
from datetime import datetime, timedelta

from src import constants


def create_dir(dir_name: str) -> pathlib.Path:
    p = pathlib.Path(dir_name)
    p.mkdir(parents=True, exist_ok=True)
    return p


def create_phone_number() -> str:
    rnd = random.randint(100000000, 999999999)
    return f"0{rnd}"


def random_true_false() -> bool:
    return random.choice([True, False])


def street_number():
    return str(random.randint(1, 128))


def get_random_from_list(list_of_things):
    return random.sample(list_of_things, k=1)[0]


def timestamp():
    return time.strftime(constants.DATE_FORMAT, time.localtime())


def old_date() -> str:
    now = datetime.now()
    old = now - timedelta(weeks=random.randint(1, 500))
    return old.strftime(constants.DATE_FORMAT)


def check_if_string(var_to_check):
    if not isinstance(var_to_check, str):
        raise ValueError(f"Wrong data type: {type(var_to_check)} ")


def combine_prefix_suffix(prefixes: list, suffixes: list) -> list:
    combinations = []
    for pre in prefixes:
        check_if_string(pre)
        for suff in suffixes:
            check_if_string(suff)
            value = f"{pre.strip()}{suff.strip()}"
            combinations.append(value.capitalize())
    return combinations


def value_from_argv_or_default():
    if len(sys.argv) == 2 and sys.argv[1].isdigit() and int(sys.argv[1]) > 0:
        return int(sys.argv[1])
    else:
        return constants.NUMBER_OF_PERSONS


def load_data_from_file(filename: str) -> list:
    data_from_file = []
    file_path = f"{constants.INDATA_DIRECTORY}/{filename}"
    with open(file_path, encoding="utf-8") as f:
        data = f.readlines()
        for line in data:
            data_from_file.append(line.strip())
    return data_from_file


def number_of_persons():
    number_of_persons = os.getenv("NUMBER_OF_PERSONS")
    if number_of_persons is not None and number_of_persons.isdigit() and int(number_of_persons) > 0:
        return int(number_of_persons)
    else:
        return constants.NUMBER_OF_PERSONS
