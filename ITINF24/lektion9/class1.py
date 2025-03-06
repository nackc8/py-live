class Greeting:
    # Konstruktor
    def __init__(self, name):
        #        print("I konstruktorn, fick namnet ", name)
        self.name = name

    def greet(self):
        print("Hello", self.name)

    def bad(self):
        print("Bad", self.name)

    def good(self):
        print("Good", self.name)


greet1 = Greeting("Fahrad")

greet1.greet()
greet1.bad()
greet1.good()
