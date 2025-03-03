p = print
# # Tillbakablick på hur datastrukturer skapas:
# en_lst = ["x"]
# en_tpl = ("x",)
# en_rng = range(3, 8)
# en_str = "x"

# En mängd, ett set, skapas via
# ett_tomt_set = set()
# p(ett_tomt_set)
# ett_set_med_innehall = set("hellohello")
# p(ett_set_med_innehall)

# tomt endast via: set()
x = {"x", "x", "x", "x"}
p(type(x), x) # <class 'set'> {'x'}
