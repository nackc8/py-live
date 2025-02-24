import myutil1

min_nya_lista = ["Björn", "Älg", "Myrslok"]

result = myutil1.get_first_second(min_nya_lista)
print("Bättre PI", myutil1.FAKE_PI)

# Sabba!
myutil1.FAKE_PI = 10

print("Förstörd PI", myutil1.FAKE_PI)

print("Resultat", result)
