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

for rubrik, rubriksinnehall in lst.items():
    print(rubrik, rubriksinnehall)
