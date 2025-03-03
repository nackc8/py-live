p = print

ppl = {
    "194502129999": {"firstname": "Torleif", "surname": "Bengtsson"},
    "191501019999": {"firstname": "Ulla", "surname": "Ullskog"},
    "192502039999": {"firstname": "Mohammed", "surname": "Larsson"},
}

for pnr in ppl.keys():
    p(pnr)

p("yngst:", min(ppl.keys()))
