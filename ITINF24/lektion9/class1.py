class Greeting:
    # Konstruktor
    def __init__(self, name):
        #        print("I konstruktorn, fick namnet ", name)
        self.name = name

    def greet(self):
        print("Hello", self.name)

    def bad(self):
        pass

    def good(self):
        pass


greet1 = Greeting("Fahrad")

greet1.greet()
