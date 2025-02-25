# slicing fungerar för alla sekvenser

lst = ["a", "b", "c", "d", "e", "f"]
by = "skinnskatteberg"

# läsning av delar

# kombinera slicing 3 och 4.

print(lst[1:5])  # omsträngens längd är exakt som ovan

# mer generellt
print(lst[1:-1])
print(by[1:-1])


# tre näst sista
print(lst[-4:-1])
print(by[-4:-1])

# tvärtom test - det kraschar inte!
print("tvärtom", lst[-1:-4])
print("tvärtom", by[-1:-4])
