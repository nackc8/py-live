def repeat_lines(line_count, content):
    result = ""
    for current_loop in range(line_count):
        result = result + "\n" + content
    return result


def textbox(content, margin):
    result = ""

    width = len(content) + 2 + margin * 2
    roof_floor = "#" * width
    sides = "#" + " " * (width - 2) + "#"
    content = "#" + content.center(width - 2, " ") + "#"

    result = result + roof_floor
    result = result + repeat_lines(margin, sides)

    result = result + "\n" + content

    result = result + repeat_lines(margin, sides)

    result = result + "\n" + roof_floor

    return result


hej_box = textbox("Hej", 3)
print(hej_box)
