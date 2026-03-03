import unittest

from ITINF25.lektion7.doctests.string_analytics import count_words


class TestStringMethods(unittest.TestCase):

    def test_not_string(self):
        with self.assertRaises(Exception):
            count_words(12345)


if __name__ == "__main__":
    unittest.main()
