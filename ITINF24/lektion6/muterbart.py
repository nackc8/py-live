# listor är muterbara, går att ändra

lst = [1, 3, 4]
print(id(lst))
lst.append("sist")
print(id(lst))

# strängar är inte muterbara

strang = "Hejsan"
print("strang, 1", strang, id(strang))
strang = strang.upper()
print("strang, 2", strang, id(strang))
greeting = "Hejsan"
print("strang, 2", greeting, id(greeting))
