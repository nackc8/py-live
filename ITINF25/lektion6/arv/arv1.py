class Parent:
    def __init__(self, name):
        self.name = name

    def greet(self, greeting):
        print(greeting, self.name)


class Child:
    pass


class ChildChild:
    pass


cc = ChildChild()
cc.greet("Hi")
