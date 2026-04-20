content = "Hej"

margin = 0
width = len(content) + 2 + margin * 2
roof_floor = "#" * width
sides = "#" + " " * (width - 2) + "#"
content = "#" + content.center(width - 2, " ") + "#"

print(roof_floor)
for current_loop in range(margin):
    print(sides)

print(content)
for current_loop in range(margin):
    print(sides)

print(roof_floor)

# fmt: off

# Mål:

#####
#Hej#     med marginal 0 -> width = content + 2
#####

# Mål med margin 2:

#########
#       #
#       #
#  Hej  #     med marginal 2 -> width = content + 2 + margin * 2
#       #
#       #
#########

# Mål med margin 1:

#######
#     #
# Hej #     med marginal 1 -> width = content + 2 + margin * 2
#     #
#######
