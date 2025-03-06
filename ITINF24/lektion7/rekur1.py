p = print
lst_of_lsts = ["a", "b", ["c", ["X"]], "d"]


def deep_print(l):
    for el in l:
        x = isinstance(el, list)
        if x == True:
            deep_print(el)
        else:
            p(el)


deep_print(lst_of_lsts)
