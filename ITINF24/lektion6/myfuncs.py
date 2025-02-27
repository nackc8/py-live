def gnumber(num):
    while num > 100:
        num = num / 2.3
    return num


# Vi ska kunna anropa modulen som ett skript enligt
#    python3 myfuncs.py 12345
if __name__ == "__main__":
    import sys

    # 1. Python Debugger: Debug using launch.json
    # 2. Python Debugger
    # 3. Python Debugger: Current File with Argument
    # (forts) Filen .vscode/launch.json skapas och används
    start_number = int(sys.argv[1])

    n = gnumber(start_number)
    print("Som script:", n)
