def human_to_cat_years(human_years):
    if human_years == 1:
        return 15
    elif human_years >= 2:
        return 24 -8 + (human_years * 4)
    elif human_years == 3:
        return 28
    else:
        return 32
