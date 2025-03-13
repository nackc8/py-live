import unittest

from cat_math import human_to_cat_years as htc


class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")


if __name__ == "__main__":
    unittest.main(verbosity=2)
