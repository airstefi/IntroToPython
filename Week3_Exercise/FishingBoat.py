budget = int(input())
season = input()
fishermen = int(input())

price = 0

if season == "Spring":
    price = 3000
    if fishermen <= 6:
        price = price - (price*0.10)
    elif 7<= fishermen<=11:
        price = price - (price*0.15)
    elif fishermen >= 12:
        price = price - (price*0.25)

elif season == "Summer" or season == "Autumn":
    price = 4200
    if fishermen <= 6:
        price = price - (price*0.10)
    elif 7 <= fishermen <= 11:
        price = price - (price*0.15)
    elif fishermen >= 12:
        price = price - (price*0.25)

elif season == "Winter":
    price = 2600
    if fishermen <= 6:
        price = price - (price*0.10)
    elif 7 <= fishermen <= 11:
        price = price - (price*0.15)
    elif fishermen >= 12:
        price = price - (price*0.25)
else:
    print("error")


if fishermen % 2 == 0 and season != "Autumn":
    price = price - (price*0.05)

diff = abs(budget - price)

if price > budget:
    print(f"Not enough money! You need {diff:.2f} leva.")
else:
    print(f"Yes! You have {diff:.2f} leva left.")