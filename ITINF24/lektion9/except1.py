standard_input = "0"

try:
    x = int(input("Skriv ett tal:"))
    resultat = 10 / x
except ZeroDivisionError as e:
    print("fel:", e)

print(resultat)
