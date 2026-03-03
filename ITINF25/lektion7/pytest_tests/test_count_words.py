from count_words import count_words


def test_hej_10():
    assert count_words("hej hej hej hej hej hej hej hej hej hej") == {"hej": 10}


def test_hopp_5():
    assert count_words("hopp hopp hopp hopp hopp") == {"hopp": 5}


def test_hej_hopp_3():
    assert count_words("hej hej hej hopp hopp hopp") == {"hej": 3, "hopp": 3}


def test_not_hopp_2():
    assert count_words("hopp hopp hopp") != {"hopp": 2}
