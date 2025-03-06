# En fabrik som ger tillbaka kompletta och
# användbara funktioner
def fun_fac():
    lst = []

    def inner_fun(obj):
        lst.append(obj)
        print(lst)

    return inner_fun


add_print = fun_fac()

add_print("Hej")

add_print("Hello")
add_print("Super")
add_print("Mario")
add_print("World")
add_print("Benny!")
