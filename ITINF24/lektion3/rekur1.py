def count_to_zero(val):
    val -= 1
    if val == 0:
        return
    print(val)
    return count_to_zero(val)
