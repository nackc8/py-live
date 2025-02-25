# slicing fungerar för alla sekvenser

lst = ["a", "b", "c", "d", "e", "f"]
by = "skinnskatteberg"


# print(lst[::-1])  # Omvänd, baklänges
# print(by[::-1])  # Omvänd, baklänges


# print(lst[2::-1])  # Börjar vid index 2
# print(by[2::-1])  # Börjar vid index 2

# print(lst[4:1:-1])  # Börjar vid index 4, slutar vid index 1 (ej inklusivt)
# print(by[4:1:-1])  # Börjar vid index 4, slutar vid index 1 (ej inklusivt)

lst = ["a", "b", "c", "d", "e", "f"]
by = "skinnskatteberg"

print(lst[4::-1])  # Börjar vid index 4, slutar vid första elementet
print(by[4::-1])  # Börjar vid index 4, slutar vid första elementet
