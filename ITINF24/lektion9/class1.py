class Greeting:
    # Konstruktor, tvingar anroparen att skicka med ett positionellt argument
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
greet2 = Greeting("My")

greet1.greet()
greet2.greet()
greet1.bad()
greet2.bad()
greet1.good()
greet2.good()
