import random


#                   .---------- * först gör att man kan få in en sekvens av positionella argument
def tal_delare(tal, *params):
    print(f"{random.randint(1, 999)} tal_delare:")
    for p in params:
        print("", "loop-snurr, p=", p)
        tal = tal / p
    return tal


# behandlat_tal = tal_delare(1000)
# behandlat_tal2 = tal_delare(1000, 2)
behandlat_tal3 = tal_delare(1000, 2, 0.5)
