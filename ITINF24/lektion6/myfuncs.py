def gnumber(num):
    while num > 100:
        num = num / 2.3
    return num


# Vi ska kunna anropa modulen som ett skript
if __name__ == "__main__":
    import sys

    # Python Debugger: Debug using launch.json / Python Debugger
    start_number = int(sys.argv[1])

    n = gnumber(9000)
    print("Mitt gnumber:", n)
    # med f-sträng
    print(f"Mitt gnumber: {n}")
