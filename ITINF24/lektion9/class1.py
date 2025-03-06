class Greeting:
    # Konstruktor
    def __init__(self, name):
        print("I konstruktorn, fick namnet ", name)

    def greet(self):
        print("Hello")

    def bad(self):
        pass

    def good(self):
        pass


greet1 = Greeting()

greet1.greet()
