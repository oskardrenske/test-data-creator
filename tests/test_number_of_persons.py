import sys
import pytest

from src import utils, constants


def test_argv_default():
    value = utils.value_from_argv_or_default()
    assert value == constants.NUMBER_OF_PERSONS


def test_value_in_args():
    value = 15
    sys.argv[1] = str(value)
    assert utils.value_from_argv_or_default() == value


@pytest.mark.parametrize("value", ["abc", "0"])
def test_neg(value):
    sys.argv[1] = str(value)
    assert utils.value_from_argv_or_default() == constants.NUMBER_OF_PERSONS
