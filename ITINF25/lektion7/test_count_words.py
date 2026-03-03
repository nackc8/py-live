from count_words import count_words

print("Test: Hej 10 gånger: ", end="")
if count_words("hej hej hej hej hej hej hej hej hej hej") != {"hej": 10}:
    raise AssertionError("Hej ska upprepas 10 gånger")
else:
    print("✓")
