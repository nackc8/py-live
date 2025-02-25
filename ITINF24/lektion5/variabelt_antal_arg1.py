import random

#        .---------- * först gör att man kan få in en sekvens av positionella argument
def xuff(*params):
    print("positionella argument:")
    for p in params:
        print("\t", p)


xuff("hej", "hopp")

xuff("")
