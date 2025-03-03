p = print

ppl = {
    "194502129999": {"firstname": "Torleif", "surname": "Bengtsson"},
    "191501019999": {"firstname": "Ulla", "surname": "Ullskog"},
    "192502039999": {"firstname": "Mohammed", "surname": "Larsson"},
}

# alt 1
# for item in ppl.items():
#     pnr = item[0]
#     if "1915" in pnr:
#         p(pnr, "heter", item[1]["firstname"])

for item in ppl.items():
    pnr = item[0]
    if "1915" in pnr:
        p(pnr, "heter", item[1]["firstname"])
