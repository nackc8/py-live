import random


#                   .---------- * först gör att man kan få in en sekvens av positionella argument
def tal_delare(tal, *params):
    print(f"{random.randint(1, 999)} positionella argument:")
    for p in params:
        print("\t", p)


tal_delare("hej", "hopp")

tal_delare("")
