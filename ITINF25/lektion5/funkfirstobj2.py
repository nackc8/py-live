lst = ["🍖", "🍕", "🍗"]

p = print


def food_sort(food):
    if food == "🍖":
        return 200
    elif food == "🍕":
        return 100
    elif food == "🍗":
        return 150
    else:
        return 0


p("Innan sortering", lst)
lst.sort()
p("Efter normal sortering", lst)
lst.sort(key=food_sort)
p("Efter egen sortering", lst)
