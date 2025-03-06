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
        ret = ret + "\n" + prefix + str(n) + " " + header
        # print(prefix, n, " ", header, sep="")
        if content:
            ret_part = indentera(content, f"{str(n)}.")
            ret = ret + ret_part
    return ret


result = indentera(global_lst)
print(result)
