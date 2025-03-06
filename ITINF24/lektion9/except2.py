standard_input = "0"

try:
    x = int(input("Skriv ett tal:"))
    resultat = 10 / x
    print(resultat)
except ZeroDivisionError as e:
    print("fel:", e)
except Exceptiona as e:
    print("okänt fel:", e)
