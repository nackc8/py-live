# operator s[i:j]
#            \  \____ tillposition (inte med positionen j, slutar med j - 1)
#             \____ startposition (från och med)
#
# om i är tomt ==> 0
# om j är tomt ==> längden (sista index + 1)

## list

lst = ["red", "yellow", "green", "teal"]
del1 = lst[:]  # Ta med alla
del2 = lst[-3:]  # Ta med de tre sista i lst
del3 = lst[:-1]  # Ta med allt utom sista elementet i lst
del4 = lst[1:-1]  # Ta med från och med index 1, till och med indexet näst sist

## string

## tuple
