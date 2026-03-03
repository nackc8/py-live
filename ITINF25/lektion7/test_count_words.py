from count_words import count_words

if count_words("hej hej hej hej hej hej hej hej hej hej") != {"hej": 10}:
    raise AssertionError("Hej ska upprepas 10 gånger")
