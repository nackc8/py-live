# fmt: off
global_lst = {
    "Bakgrund": [
        "Historia",
        "Nuläget"
    ],
    "Rapport": [
        "Sverige",
        "Finland"
    ]
}
# fmt: on

# Mål
#
# 1. Bakgrund
# 1.1 Historia
# 1.2 Nuläget
# 2. Rapport
# 2.1 Sverige
# 2.2 Finland


def indentera(lst):
    n = 0
    for header, content in lst.items():
        n += 1
        print(n, header, content)


indentera(global_lst)
