import pprint

p = pprint.pprint

# ppl har dict i sina values, deras values som är dict, har string

ppl = {
    "0502039999": {"firstname": "Bo", "surname": "Asp"},
    "1501019999": {"firstname": "Ulla", "surname": "Ullskog"},
    "2502039999": {"firstname": "Mohammed", "surname": "Larsson"},
    "4502129999": {"firstname": "Torleif", "surname": "Bengtsson"},
}
p(ppl)
