import pytest

from src import utils


@pytest.mark.parametrize(
    "prefixes, suffixes, result",
    [(["pre1"], ["suffix1"], ["Pre1suffix1"]), (["1"], ["3"], ["13"]), ([], [], [])],
)
def test_combinations_simple(prefixes, suffixes, result):
    assert utils.combine_prefix_suffix(prefixes, suffixes) == result


def test_int_expect_error():
    with pytest.raises(ValueError):
        utils.combine_prefix_suffix([1], [2])
