import smashprint

lst1 = [2, 7, 9, 15, 14, 19]
lst2 = [2, 7, 13, 25, 14, 19]


def div_by_13(lst_input):
    hit = None

    for num in lst_input:
        if num % 13 == 0:
            hit = num
    return hit


hit_for_lst1 = div_by_13(lst1)
hit_for_lst2 = div_by_13(lst2)

smashprint.smashprint("hit 1:", hit_for_lst1)
smashprint.smashprint("hit 2:", hit_for_lst2)
