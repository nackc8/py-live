def get_first_using_print_is_wrong(lst):
    print(lst[0])


def get_first(lst):
    return lst[0]


def get_first_second_kanske_mindre_lasbart(lst):
    return [lst[0], lst[1]]


# undvik globala variabler
def get_first_second_global():
    first = min_lista[0]
    second = min_lista[1]
    return [first, second]


def get_first_second(lst):
    first = lst[0]
    second = lst[1]
    return [first, second]


# i AREPL så menas None, när den skriver null

#
# Inte köra kod "i onödan" direkt i filer som
# ska importeras.
#


# min_lista = [8, 10, "Hej"]
# # tillbaka = get_first(min_lista)
# # print("tillbaka", tillbaka)
# first_second = get_first_second(min_lista)
# print("first_second", first_second)
