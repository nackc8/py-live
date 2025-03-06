standard_input = "6"

# Inbyggda exceptions: https://docs.python.org/3.11/library/exceptions.html#concrete-exceptions


try:
    x = int(input("Skriv ett tal:"))
    resultat = 10 / x
except ZeroDivisionError as e:
    print("fel:", e)
    resultat = 1
except Exception as e:
    print("okänt fel:", e)
    resultat = 0  # fix? Inga fel nedan ivf
finally:
    print("Detta steg körs allt!")

print(resultat)
