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

