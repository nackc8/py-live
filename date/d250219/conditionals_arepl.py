# AREPL requires standard_input to be hardcoded, like so: standard_input = 'hello world'; print(input())
#
# age = int(input())

# Med AREPL
standard_input = "109"  # vi leker att anv skrev 109 och tryckte enter
age = int(input())


if age >= 18:
    print("Du får köra bil!")
    print("Nää nää nääänääää")
elif age >= 16:
    print("Du får övningsköra!")
else:
    print("Du får inte köra bil!")

print("Du får även promenera!")
print("hejsan")
