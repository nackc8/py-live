# operator s[i:j:k]
#            | |  \____ hoppa k steg åt gången (negativt för baklängdes)
#            \  \____ tillposition (inte med positionen j, slutar med j - 1)
#             \____ startposition (från och med)
#
# om i är tomt ==> 0
# om j är tomt ==> längden (sista index + 1)
# om k är tomt ==> 1

## list

lst = ["red", "yellow", "green", "teal"]
# del1 = lst[::2]  # Ta varannan
# del2 = lst[::-1]  # Gå baklänges
# del3 = lst[::-2]  # Gå baklänges, varannan

## string

ord = "nackademin"
tva_forsta = ord[:2]
två_sista = ord[-2:]
baklängdes = ord[::-1]
# Rätt!
två_sista_baklängdes = baklängdes[:2]
# Allt på en gång! Experment, men inte intuitivt!
komplext = ord[:-3:-1]


## tuple
