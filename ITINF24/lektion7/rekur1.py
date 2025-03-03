lst_of_lsts = ["a", "b", ["c"], "d"]


def deep_print(l):
    for el in l:
        print(el)


deep_print(lst_of_lsts)
