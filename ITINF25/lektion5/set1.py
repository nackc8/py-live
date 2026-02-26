# Mängd, ser ut som dict men utan kolon och value
cars = {"volvo", "toyota"}

while True:
    car = input("Write a new car brand (ENTER = stop): ")
    if car == "":
        break
    if car in cars:
        print("The brand is already mentioned! Type another brand.")
        continue
    cars.add(car)

print("End result: ", cars)
