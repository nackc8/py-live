# slicing fungerar för alla sekvenser
# fast tilldelning via slice fungerar bara på "muterbara" sekvenser

# mutable vs immutable
# mutable: kan ändras
# immutable: ändras aldrig

# strängar är immutable
str1 = "hej"
print(str1, id(str1))
str1 = str1.replace("j", "y")
print(str1, id(str1))

# listor är mutable
lst = ["aa", "bb", "cc"]
print(lst, id(lst))
lst.pop()
