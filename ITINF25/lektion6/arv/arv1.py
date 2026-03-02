class Parent:
    def __init__(self, name):
        self.name = name

    def greet(self, greeting):
        print(greeting, self.name)


class Child(Parent):
    pass


class ChildChild(Child):
    pass


cc = ChildChild("Bo")
cc.greet("Hi")
