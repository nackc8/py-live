p = print


# Eller tänkt Animals() (plural)
class Zoo:
    def __init__(self):
        self.animals = []

    def add(a):
        self.animals.append(a)

    def all_sounds(self):
        for animal in self.animals:
            animal.sound()


class Animal:
    total_sounds = 0

    def __init__(self):
        self.sounds = 0

    def sound(self):
        Animal.total_sounds += 1
        self.sounds += 1

    def get_stats(self):
        stat = f"(tot: {Animal.total_sounds}, ind: {self.sounds})"
        return stat


class Eagle(Animal):
    SOUND = "Scriiish"

    # Om egen konstruktor => Inget, då behövs eget anrop super().__init__()
    def __init__(self):
        # Anropa konstruktorn i överklassen!
        super().__init__()

    def sound(self, stat=False):
        super().sound()
        print(Eagle.SOUND, end="")

        if stat:
            print(f" {self.get_stats()}", end="")

        print()


class Donkey(Animal):
    SOUND = "Ihhh ohhh"

    def __init__(self):
        super().__init__()

    def sound(self, stat=False):
        super().sound()
        if self.sounds > 2:
            print(Donkey.SOUND.upper(), end="")
        else:
            print(Donkey.SOUND, end="")

        if stat:
            print(f" {self.get_stats()}", end="")
        #            print(" " + self.get_stats(), end="")

        print()


kolmorden_zoo = Zoo()
eskilstuna_zoo = Zoo()


kolmorden_zoo.add(Eagle())
