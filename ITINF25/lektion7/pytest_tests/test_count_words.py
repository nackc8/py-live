from count_words import count_words


def test_hej_10():
    assert count_words("hej hej hej hej hej hej hej hej hej hej") == {"hej": 10}


def test_hopp_5():
    assert count_words("hopp hopp hopp hopp hopp") == {"hopp": 5}


# print("Test: hej och hopp 3 gånger: ", end="")
# if count_words("hej hej hej hopp hopp hopp") != {"hej": 3, "hopp": 3}:
#     raise AssertionError("hej och hopp ska upprepas 3 gånger")
# else:
#     print("✓")
