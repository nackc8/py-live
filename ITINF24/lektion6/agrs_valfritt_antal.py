# valfritt antal 0 ... *
def superprint(*params):
    print("in:", params)
    print()
    indrag = ""
    for param in params:
        indrag = indrag + " "
        print(f"{indrag}{param}")


superprint("hejsan", "hoppsan")
