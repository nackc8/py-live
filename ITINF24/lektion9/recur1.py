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


def indentera(flst):
    for rubrik, rubriksinnehall in flst.items():
        print(rubrik, rubriksinnehall)


indentera(global_lst)
