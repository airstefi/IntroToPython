budget = float(input())
season = input()

price = 0.0
destination = ""
place = ""

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        price = budget * 0.30
        place = "Camp"
    else:
        price = budget * 0.70
        place = "Hotel"

elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        price = budget * 0.40
        place = "Camp"
    else:
        price = budget * 0.80
        place = "Hotel"

elif budget > 1000:
    destination = "Europe"
    price = budget * 0.90
    place = "Hotel"

else:
    print("error")

print(f"Somewhere in {destination}")
print(f"{place} - {price:.2f}")