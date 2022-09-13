import pytest


def count(a, i):
    return a.count(i)


def index(a, i):
    return a.index(i)


t = (1, 2, 2, 3, 3, 3, 4, 5, 6)


@pytest.mark.parametrize("x, y, expected", [(t, 2, 2), (t, 0, 0)])
def test_count(x, y, expected):
    assert count(x, y) == expected


def test_change_element():
    a = (1, 2, 2, 3, 3, 3, 4, 5, 6)
    with pytest.raises(TypeError):
        a[0] = 9


@pytest.mark.parametrize("x, y, expected", [(t, 2, 1), (t, 0, ValueError)])
def test_index(x, y, expected):
    if type(expected) == type and issubclass(expected, Exception):
        with pytest.raises(expected):
            index(x, y)
    else:
        assert index(x, y) == expected
