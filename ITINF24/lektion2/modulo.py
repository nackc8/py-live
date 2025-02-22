print(5 % 1, "<- 0")
print(5 % 2, "<- (5 - 2*2 ) = 1")
print(5 % 3, "<- 2")
print(5 % 4)
print(5 % 5)

print(1 % 5, "<- (1 - 0*5) = 1")

# Utan modulo
num = 0
for _ in range(300):
    if num == 50:
        num = 0

    print(num)
    num += 1

# Utan modulo
num = 0
for _ in range(300):
    print(num)
    num = (num + 1) % 50
