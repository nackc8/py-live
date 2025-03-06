class AddPrint:
    def __init__(self):
        self.lista = []

    def add_print(self, part):
        self.lista.append(part)
        print(self.lista)


ap_obj1 = AddPrint()  # ny instans, egen self
ap_obj2 = AddPrint()  # igen..

ap_obj1.add_print("Hej")

ap_obj2.add_print("Hello")
ap_obj2.add_print("Super")
ap_obj2.add_print("Mario")
ap_obj2.add_print("World")
ap_obj1.add_print("Benny!")
