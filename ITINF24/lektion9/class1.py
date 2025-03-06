class Greeting:
    # Konstruktor
    def __init__(self, name):
        print("I konstruktorn, fick namnet ", name)
        self.djijji = 123

    def greet(self):
        print("Hello", self.djijji)

    def bad(self):
        pass

    def good(self):
        pass


greet1 = Greeting("Fahrad")

greet1.greet()
