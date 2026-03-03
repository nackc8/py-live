import unittest

from count_words import count_words


class TestStringMethods(unittest.TestCase):
    def test_hej_10(self):
        result = count_words("hej hej hej hej hej hej hej hej hej hej")
        self.assertEqual(result, {"hej": 10})


def test_hopp_5():
    assert count_words("hopp hopp hopp hopp hopp") == {"hopp": 5}


def test_hej_hopp_3():
    assert count_words("hej hej hej hopp hopp hopp") == {"hej": 3, "hopp": 3}


def test_not_hopp_2():
    assert count_words("hopp hopp hopp") != {"hopp": 2}


# "Eget" sätt att säkerställa att ett undantag kastas
def test_not_string_diy():
    try:
        count_words(12345)
        assert False
    except Exception:
        assert True


def test_not_string_lean_into_pytest():
    with pytest.raises(Exception):
        count_words(12345)
