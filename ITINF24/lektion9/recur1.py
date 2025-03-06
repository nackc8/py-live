# fmt: off
lst = {
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


def indentera(flst):
    for rubrik, rubriksinnehall in lst.items():
        print(rubrik, rubriksinnehall)


indentera(lst)
