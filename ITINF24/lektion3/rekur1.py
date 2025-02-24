def count_to_zero(val):
    val -= 1
    if val == 0:
        return
    print(val)
    count_to_zero(val)
