# tpl = ("hejsan", 123)

# print(tpl)

tpl2 = ("hejsan", ["hund", "katt"])

print(tpl2)
tpl2[1].append("får")
print(tpl2)

# AttributeError: 'tuple' object has no attribute 'append'
# tpl.append("123")

# TypeError: 'tuple' object does not support item assignment
# tpl[1] = 999
