# Listor är muterbara
lst = ["alfa", "beta"]

# Tuples skapas med parenteser
# Inte är muterbara
tpl = ("alfa", "beta")

for x in lst:
    print(x)

for y in tpl:
    print(y)

tpl[1] = "hej"
