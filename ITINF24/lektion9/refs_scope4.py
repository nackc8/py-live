# Inte jättebra?

lst1 = []
lst2 = []

listor = (lst1, lst2)


def lst_add_print_factory():
    # analogt till vanligt skapande: inner_lst_add_print = func
    def inner_lst_add_print(ndx, obj):
        lst = listor[ndx]
        lst.append(obj)
        print(lst)

    return inner_lst_add_print


funk_igen = inner_lst_add_print

inner_lst_add_print(1, "Hej")

inner_lst_add_print(0, "Hello2")
inner_lst_add_print(0, "Super")
inner_lst_add_print(0, "Mario")
inner_lst_add_print(0, "World")
inner_lst_add_print(1, "Benny!")
