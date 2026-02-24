points = [783, 27, 49, -199, 88]

res = []

for point in points:
    if point > 0:
        res.append(point // 2)

# Med list comprehension

res2 = [point // 2 for point in points if point > 0]
