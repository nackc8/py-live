from cat_math import human_to_cat_years as htc


class TestStringMethods(unittest.TestCase):
    def test_one(self):
        self.assertEqual(htc(1), 15)

    def test_two(self):
        self.assertEqual(htc(2), 24)

    def test_three(self):
        self.assertEqual(htc(3), 28)

    def test_four(self):
        self.assertEqual(htc(4), 32)

    def test_eighteen(self):
        self.assertEqual(htc(18), 88)


if __name__ == "__main__":
    unittest.main(verbosity=2)
