# *names = den tar ALLA positionella argument
def greet(*names, greeting="Hej"):
    print("names typ: ", type(names))
    for name in names:
        print(greeting, name)


greet("Mayank", "Ulla", "Xi", "Bengt", "Mohammad")
greet("Mayank", "Ulla", "Xi", "Bengt", "Mohammad", greeting="Yoyoyo")
