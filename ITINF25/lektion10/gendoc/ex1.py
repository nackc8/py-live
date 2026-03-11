class Greetings:
    def __init__(self):
        self.parts = []

    def addGreeting(self, text):
        self.parts.append(text)


g = Greetings()

g.addGreeting("Terve").addGreeting("Hej")

print("Slut")
