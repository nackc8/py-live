# En datatyp kan antingen vara immutable, då kan den inte
# ändras när man skapat. Eller så kan den vara
# mutable, då kan den ändras.

# strängar är immutable = de kan dela på samma minnesadress
obj1 = "hej"
obj2 = "hej"
obj1_id = id(obj1)
obj2_id = id(obj2)

print(obj1_id, obj2_id)

# int är immutable

print(id(2))
print(id(2))

# float är immutable
print(id(3.14))
print(id(3.14))

# boolean är immutable
print(id(True))
print(id(True))

# list är MUTABLE

lst1_hundar = ["papillion", "chefrrr"]
lst2_hundar = ["papillion", "chefrrr"]
print(id(lst1_hundar))
print(id(lst2_hundar))

lst3_hundar = lst1_hundar
print(id(lst3_hundar))

# Eftersom de pekar på samma muterbara objekt, ändras båda om man ändrar en
lst1_hundar.append("tax")
print(lst1_hundar)
print(lst3_hundar)

# Om jag vill ha en EGEN kopia av en lista, inte dela
lst_egen2_hundar = list(lst1_hundar)
print(id(lst1_hundar))
print(id(lst_egen2_hundar))
lst1_hundar.append("mops")

print(lst1_hundar)
print(lst_egen2_hundar)

# Ett till sätt att få en egen kopia
lst_egen3_hundar = lst1_hundar.copy()

print(id(lst1_hundar))
print(id(lst_egen3_hundar))
lst1_hundar.append("mops")

print(lst1_hundar)
print(lst_egen3_hundar)
