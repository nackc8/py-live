standard_input = "0"

# Inbyggda exceptions: https://docs.python.org/3.11/library/exceptions.html#concrete-exceptions

try:
    x = int(input("Skriv ett tal:"))
    resultat = 10 / x
    print(resultat)
except ZeroDivisionError as e:
    print("fel:", e)
except Exceptiona as e:
    print("okänt fel:", e)
