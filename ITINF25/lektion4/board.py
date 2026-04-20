rook = "♜"
empty = "x"

# fmt: off
board = [
    [rook,empty,empty,empty,empty,empty,empty,empty],
    [empty,empty,empty,empty,empty,empty,empty,empty],
    [empty,empty,empty,empty,empty,empty,empty,empty],
    [empty,empty,empty,rook,empty,empty,empty,empty],
    [empty,empty,empty,empty,empty,empty,empty,empty],
    [empty,empty,empty,empty,empty,empty,empty,empty],
    [empty,empty,empty,empty,empty,empty,empty,empty],
    [rook,empty,empty,empty,empty,empty,empty,empty],
]
# fmt: on

for row in board:
    for col in row:
        print(col, end="")
    print()
