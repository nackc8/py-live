import pprint

p = pprint.pprint

ppl = {
    "4502129999": {"firstname": "Torleif", "surname": "Bengtsson"},
    "1501019999": {"firstname": "Ulla", "surname": "Ullskog"},
    "2502039999": {"firstname": "Mohammed", "surname": "Larsson"},
}
ppl["0502039999"] = {"firstname": "Bo", "surname": "Asp"}

# p(ppl.keys())  # som en lista med personnummer i detta fall

p(ppl.values())
# ger:
# [
#     {"firstname": "Torleif", "surname": "Bengtsson"},
#     {"firstname": "Ulla", "surname": "Ullskog"},
#     {"firstname": "Mohammed", "surname": "Larsson"},
#     {"firstname": "Bo", "surname": "Asp"},
# ]
