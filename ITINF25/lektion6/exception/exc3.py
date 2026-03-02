def delat_med_ett(divisor):
    try:
        result = 1 / divisor
        return result
    except ZeroDivisionError as e:
        print("We handle ZeroDivisionError", e)
        return 0


res = delat_med_ett("hej")
print(res)
