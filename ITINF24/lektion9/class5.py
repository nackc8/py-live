p = print


class Animal:
    total_sounds = 0

    def __init__(self):
        self.sounds = 0

    def sound(self):
        Animal.total_sounds += 1
        self.sounds += 1


class Eagle(Animal):
    # Om egen konstruktor => Inget, då behövs eget anrop super().__init__()
    def __init__(self):
        # Anropa konstruktorn i överklassen!
        super().__init__()

    def sound(self):
        super().sound()
        stat = f"(tot: {Animal.total_sounds}, ind: {self.sounds})"
        print("Scriiish", stat)


# class Donkey:
#     total_sounds = 0

#     def __init__(self):
#         self.sounds = 0

#     def sound(self):
#         Donkey.total_sounds += 1
#         self.sounds += 1
#         stat = f"(tot: {Donkey.total_sounds}, ind: {self.sounds})"
#         print("Ihhh ohh ohhh", stat)


eagle1 = Eagle()  # Animal!!!
eagle1.sound()

eagle2 = Eagle()  # Animal!!!
eagle2.sound()
eagle2.sound()

# donkey = Donkey()
# donkey.sound()
# donkey.sound()
# donkey.sound()
# donkey.sound()
