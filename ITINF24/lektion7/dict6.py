p = print

ppl = {
    "194502129999": {"firstname": "Torleif", "surname": "Bengtsson"},
    "191501019999": {"firstname": "Ulla", "surname": "Ullskog"},
    "192502039999": {"firstname": "Mohammed", "surname": "Larsson"},
}

for pdata in ppl.values():
    p(pdata["firstname"])

namn = [pdata["firstname"] for pdata in ppl.values()]
namn = [n.upper() for n in namn]
