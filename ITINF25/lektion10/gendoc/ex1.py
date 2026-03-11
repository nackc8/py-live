class GreetingsFluent:
    def __init__(self):
        self.parts = []

    def addGreeting(self, text):
        self.parts.append(text)


g = GreetingsFluent()

g.addGreeting("Terve")
g.addGreeting("Hej")


class GreetingsFluent:
    def __init__(self):
        self.parts = []

    def addGreeting(self, text):
        self.parts.append(text)
        return self


g = GreetingsFluent()

g.addGreeting("Terve").addGreeting("Hej")

print("Slut")
