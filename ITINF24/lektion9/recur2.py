# fmt: off
global_lst = {
    "Bakgrund": {
        "Historia": False,
        "Nuläget": False
    },
    "Rapport": {
        "Sverige": False,
        "Finland": False
    }
}
# fmt: on

# Mål: returnera en sträng med allt nedan
#
# 1. Bakgrund
# 1.1 Historia
# 1.2 Nuläget
# 2. Rapport
# 2.1 Sverige
# 2.2 Finland


def indentera(dct, prefix=""):
    ret = ""
    n = 0
    for header, content in dct.items():
        n += 1
        ret = prefix + str(n) + " "
        print(prefix, n, " ", header, sep="")
        if content:
            indentera(content, f"{str(n)}.")


indentera(global_lst)
