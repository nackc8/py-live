p = print


class Eagle:
    total_sounds = 0

    def sound(self):
        total_sounds += 1
        print("Scriiish")


class Donkey:
    total_sounds = 0

    def sound(self):
        print("Ihhh ohhh")


eagle1 = Eagle()
eagle1.sound()

donkey = Donkey()
donkey.sound()
