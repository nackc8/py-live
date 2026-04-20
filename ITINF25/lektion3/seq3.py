# Länk: https://docs.python.org/3.13/library/stdtypes.html#sequence-types-list-tuple-range

# sekvensär är till exempel
# string
# list
# tuple (inte sett ännu)

seq = ["aa", "bb", "cc", "dd", "ee"]

# Slicing

# Från och med pos 1, till 3 (slutar på 1)
print(seq[1:3])

# Från och med pos 0, till 2 (slutar på 1)
print(seq[:2])

# Från och med pos 0, till slutet
print(seq[3:])

# Från och med tre pos från slutet, till slutet
print(seq[-3:])

# Vänd på listan
print(seq[::-1])

# Vänd på listan och visa från pos 2 efteråt
print(seq[2::-1])
