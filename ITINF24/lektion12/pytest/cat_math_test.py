import pytest
from cat_math import human_to_cat_years as htc


def test_one():
    assert htc(1), 15


def test_two():
    assert htc(2), 24


def test_three():
    assert htc(3), 28


def test_four():
    assert htc(4), 32


def test_eighteen():
    assert htc(18), 88


if __name__ == "__main__":
    pytest.main(["-v"])
