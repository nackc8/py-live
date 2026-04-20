def repeat_lines(content, line_count):
    result = ""
    for _ in range(line_count):
        result = result + "\n" + content
    return result


# Länk: https://docs.python.org/3/tutorial/controlflow.html#positional-or-keyword-arguments
#
# def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
#       -----------    ----------     ----------
#         |             |                  |
#         |        Positional or keyword   |
#         |                                - Keyword only
#          -- Positional only


def textbox(
    content,
    /,
    margin=0,
    *,
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


name = input("Vad är ditt namn? ")

name_box = textbox(
    name,
    2,
    ch_topleft="┏",
    ch_horiz="━",
    ch_topright="┓",
    ch_vert="┃",
    ch_bottomleft="┗",
    ch_bottomright="┛",
)

print(name_box)

name = input("Vad är ditt namn? ")

name_box = textbox(
    name,
)

print(name_box)

name = input("Vad är ditt namn? ")

name_box = textbox(
    name,
    ch_topleft="/",
    ch_horiz="-",
    ch_vert="|",
    ch_topright="\\",
    ch_bottomleft="\\",
    ch_bottomright="/",
)

print(name_box)

# Tecken från UTF-8-delen "Box Drawing"
#
# ┏━┓
# ┃ ┃
# ┗━┛
#
# ╭──╮
# │  │
# ╰──╯
