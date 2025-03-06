
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
