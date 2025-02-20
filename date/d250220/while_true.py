sum = 0

while True:
    num = input("Skriv ett heltal eller exit: ")
    if num.isdigit():
        sum += int(num)
    elif num.capitalize() == "Exit":
        break
    else:
        print("Du skrev varken en siffra eller exit!")

print("Summan är", sum)
