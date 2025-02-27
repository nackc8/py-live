def tva_tal(n, nagot_annat):
    return (n * 2, nagot_annat * 5)


result1 = tva_tal(10, 38)
tal1 = result1[0]
tal2 = result1[1]
print(f"tal1: {tal1} tal2: {tal2}")

# "unpacking"
a, b = tva_tal(10, 38)
print(f"a {a} b {b}")
