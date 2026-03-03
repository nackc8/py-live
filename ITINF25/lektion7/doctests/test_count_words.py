import unittest

from ITINF25.lektion7.doctests.string_analytics import count_words


class TestStringMethods(unittest.TestCase):



    def test_hej_hopp_3(self):
        result = count_words("hej hej hej hopp hopp hopp")
        self.assertEqual(result, {"hej": 3, "hopp": 3})

    def test_not_hopp_2(self):
        result = count_words("hopp hopp hopp")
        self.assertNotEqual(result, {"hopp": 2})

    def test_not_string(self):
        with self.assertRaises(Exception):
            count_words(12345)


if __name__ == "__main__":
    unittest.main()
