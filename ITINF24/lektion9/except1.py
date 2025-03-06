standard_input = "0"

x = int(input("Skriv ett tal:"))

try:
    resultat = 10 / x
except Exception as vadmanvill:
    print("fel:", vadmanvill)

print(resultat)
