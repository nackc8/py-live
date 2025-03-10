class Cart:
    def __init__(self):
        self.content = {}

    def add(self, article, qty):
        # Alt sätt: (istället för .get(key,default)
        #
        # if article in self.content:
        #     self.content[article] = self.content["article"] + qty
        # else:
        #     self.content[article] = qty

        self.content[article] = self.content.get(article, 0) + qty


cart_one = Cart()
cart_one.add("fanta", 2)
cart_one.add("fanta", 1)

cart_two = Cart()
cart_two.add("mjölk", 1)

input("Press enter...")
