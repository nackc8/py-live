p = print
lst_of_lsts = ["a", "b", ["c"], "d"]


def deep_print(l):
    for el in l:
        x = isinstance(el, list)
        p(x)
        print(el)


deep_print(lst_of_lsts)
