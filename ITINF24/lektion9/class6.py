p = print


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

    def sound(self):
        super().sound()
        print(Eagle.SOUND, self.get_stats())


class Donkey(Animal):
    SOUND = "Ihhh ohhh"

    def __init__(self):
        super().__init__()

    def sound(self, stat=False):
        super().sound()
        if self.sounds > 2:
            print(Donkey.SOUND.upper())
        else:
            print(Donkey.SOUND)


eagle1 = Eagle()  # Animal!!!
eagle1.sound()

eagle2 = Eagle()  # Animal!!!
eagle2.sound()
eagle2.sound()

donkey = Donkey()
donkey.sound(True)
donkey.sound()
donkey.sound()
donkey.sound()
