p = print


class Eagle:
    total_sounds = 0

    def __init__(self):
        self.sounds = 0

    def sound(self):
        Eagle.total_sounds += 1
        stat = f"(tot: {Eagle.total_sounds}, ind: {9876})"
        print("Scriiish", stat)


class Donkey:
    total_sounds = 0

    def sound(self):
        Donkey.total_sounds += 1
        stat = f"(tot: {Donkey.total_sounds}, ind: {9876})"
        print("Ihhh ohhh", stat)


eagle1 = Eagle()
eagle1.sound()

eagle2 = Eagle()
eagle2.sound()

donkey = Donkey()
donkey.sound()
