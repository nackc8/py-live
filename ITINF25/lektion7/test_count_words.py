from count_words import count_words

print("Test: Hej 10 gånger: ", end="")
if count_words("hej hej hej hej hej hej hej hej hej hej") != {"hej": 10}:
    raise AssertionError("hej ska upprepas 10 gånger")
else:
    print("✓")

print("Test: Hopp 5 gånger: ", end="")
if count_words("hopp hopp hopp hopp hopp") != {"hopp": 5}:
    raise AssertionError("hopp ska upprepas 5 gånger")
else:
    print("✓")
