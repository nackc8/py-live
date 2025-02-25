import random


#                   .---------- * först gör att man kan få in en sekvens av positionella argument
def tal_delare(tal, *params):
    print(f"{random.randint(1, 999)} positionella argument:")
    for p in params:
        tal = tal / p
        print(tal)
    return tal


behandlat_tal = tal_delare(1000)
# behandlat_tal2 = tal_delare(1000, 2)
