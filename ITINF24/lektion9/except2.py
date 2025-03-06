standard_input = "hej"

try:
    x = int(input("Skriv ett tal:"))
    resultat = 10 / x
    print(resultat)
except ZeroDivisionError as e:
    print("fel:", e)
except Exception as e:
    print("okänt fel:", e)
