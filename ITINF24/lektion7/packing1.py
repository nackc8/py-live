# * först i funk definition
#      = packing
def p(*args, **kwargs):
    # * först i funk-anrop
    #      = unpacking (inte 100% på termen)
    print(*args, **kwargs)
    # samma som
    print(1, 2, sep=":", end="THE END")

p(1, 2, sep=":")
