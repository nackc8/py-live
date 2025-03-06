# Inte jättebra?

lst1 = []
lst2 = []

listor = (lst1, lst2)

minvar = 123  # Tilldela vanlig variabel


def lst_add_print(ndx, obj):
    lst = listor[ndx]
    lst.append(obj)
    print(lst)

funk_igen = lst_add_print

lst_add_print(1, "Hej")

lst_add_print(0, "Hello2")
lst_add_print(0, "Super")
lst_add_print(0, "Mario")
lst_add_print(0, "World")
lst_add_print(1, "Benny!")
