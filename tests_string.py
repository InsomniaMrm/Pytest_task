import pytest


def lower_case(x):
    return x.lower()


def contains(x, y):
    return y in x


def test_lower_case():
    assert lower_case('DRAGON') == 'dragon'


def test_raises_exception_on_non_string_arguments():
    with pytest.raises(AttributeError):
        lower_case(9)


@pytest.mark.parametrize("x, y, expected", [("DRAGONS", "GON", True), ("HOME", "AA", False)])
def test_contains(x, y, expected):
    assert contains(x, y) == expected
