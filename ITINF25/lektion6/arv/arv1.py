class Parent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hi", self.name)


class Child(Parent):
    def bye(self):
        print(f"{self.name} says goodbye!")


cc = Child("Bo")
cc.greet()
