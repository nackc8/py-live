# En fabrik som ger tillbaka kompletta och
# användbara funktioner
def fun_fac():
    lst = []

    def inner_fun(obj):
        lst.append(obj)
        print(lst)

    return inner_fun


add_print1 = fun_fac()
add_print2 = fun_fac()

add_print1("Hej")

add_print2("Hello")
add_print2("Super")
add_print2("Mario")
add_print2("World")
add_print1("Benny!")
