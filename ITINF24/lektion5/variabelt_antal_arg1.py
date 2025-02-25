import random


#        .---------- * först gör att man kan få in en sekvens av positionella argument
def xuff(*params):
    print(f"{random.randint(1, 999)} positionella argument:")
    for p in params:
        print("\t", p)

xuff("hej", "hopp")

xuff("")
