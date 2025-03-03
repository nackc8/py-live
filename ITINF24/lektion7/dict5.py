p = print

ppl = {
    "4502129999": {"firstname": "Torleif", "surname": "Bengtsson"},
    "1501019999": {"firstname": "Ulla", "surname": "Ullskog"},
    "2502039999": {"firstname": "Mohammed", "surname": "Larsson"},
}

for pnr in ppl.keys():
    p(pnr)

p("yngst:", min(ppl.keys()))
