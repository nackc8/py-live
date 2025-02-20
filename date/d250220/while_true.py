# Om while-uttrycket är False körs ingen snurr i loopen

sum = 0

while True:
    num = input("Skriv ett heltal eller exit: ")
    if num.isdigit():
        sum += int(num)
