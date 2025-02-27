# i doc: x in s
#    True if an item of s is equal to x, else False

lst = ["myrslok", "apa", "björn"]
strang = "min myrslok umgås inte med min apa, men med min björn"
tpl = ("orm", "sköldpadda", "hamster", "ekorre")

active = tpl

moddad = tpl + (1, 2)

apa_finns = "apa" in active
baver = "bäver" in active

# len(s): length of s
#     length of s
print(len(active))

# max(s)
# largest item of s
print(max(active))

for part in active:
    print("del:", part)
