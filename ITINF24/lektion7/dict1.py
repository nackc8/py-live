p = print

x = {}

p(type(x), x, len(x))


# dict är lite som list här, indexet är ett ord istället för heltal i detta fall
x["indoktrinera"] = "Styrd påverkan"
x["pizza"] = "Platt mat"
x[789] = "Ett högre än 788"

p(f"indoktrinera betyder {x['indoktrinera']}")
p(f"pizza betyder {x['pizza']}")

p("hela:", x)

x2 = {"indoktrinera": "Styrd påverkan", "pizza": "Platt mat", 789: "Ett högre än 788"}
