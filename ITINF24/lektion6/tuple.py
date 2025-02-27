# tuple

# tom tuple, tomma parenteser
tpl1 = ()

# tuple med ett element har komma sist
tpl1 = (5.3,)

# tuple ska inte kunna muteras, så
# den får inte ha något muterbart
# i sig...
tpl2 = ()

lst = [1, 3, 4]
print(id(lst))
lst.append("sist")
print(id(lst))

listan = [1, 2, 3]  # muterbart i icke-muterbart?
min_tupel_med_lista = ("Hej", 1, True, 3.3, listan)
print(min_tupel_med_lista)
listan.append("en till")
print(min_tupel_med_lista)
# Japp, det gick!
