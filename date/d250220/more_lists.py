numbers = [1, 2, 3, 4, 5]

pos_3_in_numbers = numbers[3]

print(numbers[0])  # prints 1

# TODO: Vi gör en egen funktion som kan ta ut flera index på en gång!
pos_1_in_numbers = numbers[1]
pos_4_in_numbers = numbers[4]

# [" ", "X", " "],
# ["O", "X", "O"],
# [" ", " ", "X"]
tic_tac_toe = [[" ", "X", " "], ["O", "X", "O"], [" ", " ", "X"]]

# if sats som kollar om X har vunnit diagonalt från högst upp
# till vänster, till längst ned till höger

# Ej vunnit

if tic_tac_toe[0][0] == "X" and tic_tac_toe[1][1] == "X" and tic_tac_toe[2][2] == "X":
    print("X vann diagonalt från övre vänstra hörnet, till nedre högra")
else:
    print("X har inte vunnit ännu..")

tic_tac_toe[0][0] = "X"

# Nu vunnit

if tic_tac_toe[0][0] == "X" and tic_tac_toe[1][1] == "X" and tic_tac_toe[2][2] == "X":
    print("X vann diagonalt från övre vänstra hörnet, till nedre högra")
else:
    print("X har inte vunnit ännu..")
