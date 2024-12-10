import pytest

from src import utils


def test_phone_number():
    number = utils.create_phone_number()
    assert len(number) == 10
    assert number.isdigit()
    assert number[0] == "0"
    assert isinstance(number, str)


def test_street_number():
    number = utils.street_number()
    assert len(number) <= 3
    assert number.isdigit()
    assert int(number) <= 128


@pytest.mark.parametrize(
    "input_list, expected_type",
    [([1, 2, 3], int), (["1", "2", "3"], str), ([True, False], bool)],
)
def test_get_random_from_list(input_list, expected_type):
    random_value = utils.get_random_from_list(input_list)
    assert random_value in input_list
    assert isinstance(random_value, expected_type)


def test_timestamp():
    ts = utils.timestamp()
    assert len(ts) == 17
    assert ts.startswith("20")  # will break on January 1, 2100


def test_old_date():
    ts = utils.old_date()
    assert len(ts) == 17
    assert ts.startswith("20")  # will break on January 1, 2100


def test_get_true_false():
    result = utils.random_true_false()
    assert result is True or result is False
