import pprint

p = pprint.pprint

# en dict med en nyckel, "4502129999" som har värdet None
ppl_v0 = {"4502129999": None}

ppl_v1 = {
    "4502129999": {"firstname": "Torleif", "surname": "Bengtsson"},
    "1501019999": {"firstname": "Ulla", "surname": "Ullskog"},
    "2502039999": {"firstname": "Mohammed", "surname": "Larsson"},
}

ppl_v1["0502039999"] = {"firstname": "Bo", "surname": "Asp"}

p(ppl_v1)
