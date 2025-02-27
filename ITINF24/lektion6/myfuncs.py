def gnumber(num):
    while num > 100:
        num = num / 2.3
    return num


if __name__ == "__main__":
    n = gnumber(9000)
    print("Mitt gnumber:", n)
    # med f-sträng
    print(f"Mitt gnumber: {n}")
