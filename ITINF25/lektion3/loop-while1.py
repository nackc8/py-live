import random

total = 1

# total % 2 == 0 --> Om jämnt delbart med 2 så kommer 0 ut
# total % 5 == 0 --> Om jämnt delbart med 5 så kommer 0 ut

while total < 30:
    if total % 2 == 0 and total > 20:
        print("Very special", total)
        total = total + 1
        # Hoppar till nästa
        continue
    if total % 5 == 0 and total > 24:
        print("Aborting early", total)
        break
    print("The number is", total)
    total = total + random.randint(1, 10)

print("Result", total)
