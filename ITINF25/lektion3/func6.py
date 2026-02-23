def repeat_lines(content, line_count):
    result = ""
    for _ in range(line_count):
        result = result + "\n" + content
    return result


def textbox(
    content,
    margin=0,
    ch_topleft="#",
    ch_horiz="#",
    ch_topright="#",
    ch_vert="#",
    ch_bottomleft="#",
    ch_bottomright="#",
):
    result = ""

    width = len(content) + 2 + margin * 2
    roof = ch_topleft + ch_horiz * (width - 2) + ch_topright
    sides = ch_vert + " " * (width - 2) + ch_vert
    content = ch_vert + content.center(width - 2, " ") + ch_vert

    result = result + roof
    result = result + repeat_lines(sides, margin)

    result = result + "\n" + content

    result = result + repeat_lines(sides, margin)

    floor = ch_bottomleft + ch_horiz * (width - 2) + ch_bottomright
    result = result + "\n" + floor

    return result


hej_box = textbox(
    content="Hej",
    margin=5,
    ch_topleft="┏",
    ch_horiz="━",
    ch_topright="┓",
    ch_vert="┃",
    ch_bottomleft="┗",
    ch_bottomright="X",
)
print(hej_box)

# Tecken från UTF-8-delen "Box Drawing"
#
# ┏━┓
# ┃ ┃
# ┗━┛
#
# ╭──╮
# │  │
# ╰──╯
