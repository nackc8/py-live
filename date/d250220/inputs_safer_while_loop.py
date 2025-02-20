import sys


age = input("Ålder? ")

if not age.isdigit():
    print("Ange en siffra")
    sys.exit(1)

age = int(age)

age_in_five_years = age + 5

print("Om fem år är du ", age_in_five_years, "år gammal")
