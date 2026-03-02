class Human:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hi", self.name)


class Police(Human):
    def greet(self):
        print("Halt!")

    def bye(self):
        print(f"{self.name} says goodbye!")


class Military(Human):
    def greet(self):
        print("Skott kommer!")


cc = Police("Bo")
cc.greet()
cc.bye()
