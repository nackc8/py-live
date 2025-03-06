# Inte jättebra?

lst1 = []
lst2 = []

listor = (lst1, lst2)

# En funktion, kan ge tillbaka en funktion
# som jag kan använda.
#
# liknar följande då vi också har en funktionspekare i en variabel:
# p = print


# En fabrik som ger tillbaka funktioner
def lst_add_print_factory():
    # analogt till vanligt skapande: inner = func
    def inner(ndx, obj):
        lst = listor[ndx]
        lst.append(obj)
        print(lst)

    return inner


inner_lst_add_print = lst_add_print_factory()

funk_igen = inner_lst_add_print

inner_lst_add_print(1, "Hej")

inner_lst_add_print(0, "Hello")
inner_lst_add_print(0, "Super")
inner_lst_add_print(0, "Mario")
inner_lst_add_print(0, "World")
inner_lst_add_print(1, "Benny!")
