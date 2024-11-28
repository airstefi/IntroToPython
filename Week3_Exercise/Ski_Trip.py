days = int(input())
acc = input()
rating = input()

price = 0
days = days -1

if acc == "room for one person":
    price = days * 18.00

elif acc == "apartment":
    price = days * 25.00
    # print(price)
    if days < 10:
        price = price - (price*0.3)
    elif 10 <= days <= 15:
        price = price - (price*0.35)
        # print(price)
    else:
        price = price - (price*0.5)

else:
    price = days * 35

    if days < 10:
        price = price - (price*0.1)
    elif 10<=days<=15:
        price = price - (price*0.15)
    else:
        price = price - (price*0.20)

if rating == "positive":
    price = price + (price*0.25)
else:
    price = price - (price*0.1)


print(f"{price:.2f}")