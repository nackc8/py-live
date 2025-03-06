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


def indentera(flst):
    n = 0
    for rubrik, rubriksinnehall in flst.items():
        n += 1
        print(rubrik, rubriksinnehall)


indentera(global_lst)
