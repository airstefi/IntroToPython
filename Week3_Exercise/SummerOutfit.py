degrees = int(input())
timeofday = input()

outfit = ""
shoes = ""

if timeofday == "Morning":
    if 10<=degrees<=18:
        shoes = "Sneakers"
        outfit = "Sweatshirt"
    elif 18<degrees<=24:
        shoes = "Moccasins"
        outfit = "Shirt"
    elif degrees>= 25:
        shoes = "Sandals"
        outfit = "T-Shirt"
    else:
        print("error")
elif timeofday == "Afternoon":
    if 10<=degrees<=18:
        shoes = "Moccasins"
        outfit = "Shirt"
    elif 18<degrees<=24:
        shoes = "Sandals"
        outfit = "T-Shirt"
    elif degrees>= 25:
        shoes = "Barefoot"
        outfit = "Swim Suit"
    else:
        print("error")
elif timeofday == "Evening":
    if 10<=degrees<=18:
        shoes = "Moccasins"
        outfit = "Shirt"
    elif 18<degrees<=24:
        shoes = "Moccasins"
        outfit = "Shirt"
    elif degrees>= 25:
        shoes = "Moccasins"
        outfit = "Shirt"
    else:
        print("error")
else:
    print("error")

print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")