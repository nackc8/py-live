# En fabrik som ger tillbaka kompletta och
# användbara funktioner
def fun_fac():
    # analogt till vanligt skapande: inner = func
    def inner_fun(ndx, obj):
        lst = listor[ndx]
        lst.append(obj)
        print(lst)

    return inner_fun


inner_lst_add_print = fun_fac()

funk_igen = inner_lst_add_print

inner_lst_add_print(1, "Hej")

inner_lst_add_print(0, "Hello")
inner_lst_add_print(0, "Super")
inner_lst_add_print(0, "Mario")
inner_lst_add_print(0, "World")
inner_lst_add_print(1, "Benny!")
