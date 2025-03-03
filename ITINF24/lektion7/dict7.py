p = print

ppl = {
    "194502129999": {"firstname": "Torleif", "surname": "Bengtsson"},
    "191501019999": {"firstname": "Ulla", "surname": "Ullskog"},
    "192502039999": {"firstname": "Mohammed", "surname": "Larsson"},
}

for item in ppl.items():
    pnr = item[0]
    if "195001019999" > pnr:
        p(pnr)
