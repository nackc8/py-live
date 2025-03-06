# Skalar inte, eller hur?

lst1 = []
lst2 = []


def lst1_add_print(obj):
    lst1.append(obj)
    print(lst1)


def lst2_add_print(obj):
    lst2.append(obj)
    print(lst2)


lst2_add_print("Hej")

lst1_add_print("Hello")
lst1_add_print("Super")
lst1_add_print("Mario")
lst1_add_print("World")
lst2_add_print("Benny!")
