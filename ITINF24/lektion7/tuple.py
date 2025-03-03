tal = print
p = tal

t1 = ("Ove", 67)

# samma som:
#    name = t1[0]
#    agee = t1[1]
name, age = t1

p("t1", type(t1), t1)

p("name", type(name), name)

# uttrycket till höger är en
# tuple, men det försvinner direkt
# då vi endast sparar delarna i
# variablerna name, age.
name, age = "Janne", 55

# Bäst att skriva tuples med
# parenteser, då utan inte alltid
# fungerar och är mindre tydligt
name, age = ("Janne", 55)
