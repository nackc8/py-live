# Global - den står utan indentering
calls = 1


def hello():
    haha_count = 3

    def haha():
        # För att kunna skriva till en variabel från ett yttre scope
        nonlocal haha_count
        haha_count = haha_count + 1
        hahastring = "ha" * haha_count
        return hahastring

    res = haha()
    print(res)
    res = haha()
    print(res)


hello()
