def hej():
    content = "Hej"

    result = ""

    margin = 1
    width = len(content) + 2 + margin * 2
    roof_floor = "#" * width
    sides = "#" + " " * (width - 2) + "#"
    content = "#" + content.center(width - 2, " ") + "#"

    result = result + roof_floor
    for current_loop in range(margin):
        result = result + "\n" + sides

    result = result + "\n" + content

    for current_loop in range(margin):
        result = result + "\n" + sides

    result = result + "\n" + roof_floor

    return result


hej_box = hej()
print(hej_box)
