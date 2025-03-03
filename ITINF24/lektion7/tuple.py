def p(*args, **kwargs):
    print(*args, **kwargs)
    # samma som
    print(1, 2, sep=":")


p(1, 2, sep=":")
