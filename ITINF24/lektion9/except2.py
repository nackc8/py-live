standard_input = "hej"

# Inbyggda exceptions: https://docs.python.org/3.11/library/exceptions.html#concrete-exceptions

try:
    x = int(input("Skriv ett tal:"))
    resultat = 10 / x
    print(resultat)
except ZeroDivisionError as e:
    print("fel:", e)
except Exception as e:
    print("okänt fel:", e)
