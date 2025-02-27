import random


#                   .---------- * först gör att man kan få in en sekvens av positionella argument
def tal_delare(tal, *params, faktor):
    """tal_delare delar ett tal med var och en
    av parametrarna i param"""
    print(f"{random.randint(1, 999)} tal_delare:")
    for p in params:
        print("", "loop-snurr, p=", p)
        tal = (tal / p) * faktor
    return tal


# behandlat_tal = tal_delare(1000)
# behandlat_tal2 = tal_delare(1000, 2)
behandlat_tal3 = tal_delare(1000, 2, 0.5, 3, 4, faktor=1)
