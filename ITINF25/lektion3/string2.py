name = "Viktoria"
greeting = f"Hej {name}!"

print(greeting)


def scream(content):
    return content.upper()


print(f"Hejdå {name}")
print(f"Hejdå {name * 2}")
print(f"Hejdå {name.replace('i', 'u')}")
print(f"Hejdå {scream(name)}")
