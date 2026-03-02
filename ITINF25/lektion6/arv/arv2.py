class Human:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hi", self.name)

    def bye(self):
        print(f"{self.name} vi ses")


class Police(Human):
    def greet(self):
        print("Halt!")

    def bye(self):
        print(f"{self.name} says goodbye!")


class Military(Human):
    def __init__(self, name):
        self.grade = "korpral"

    def greet(self):
        print("Skott kommer!")


cc = Military("Bo")
cc.greet()
cc.bye()
