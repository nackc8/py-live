from cat_math import human_to_cat_years as htc


def prod(a, b):
    return a * b


def test_one():
    self.assertEqual(htc(1), 15)


def test_two():
    self.assertEqual(htc(2), 24)


def test_three():
    self.assertEqual(htc(3), 28)


def test_four():
    self.assertEqual(htc(4), 32)


def test_eighteen():
    self.assertEqual(htc(18), 88)


if __name__ == "__main__":
    unittest.main(verbosity=2)
