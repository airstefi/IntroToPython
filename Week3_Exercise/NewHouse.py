flower = input()
numflowers = int(input())
budget = int(input())

price = 0

if flower == "Roses":
    price = numflowers*5.00
    if numflowers > 80:
        price = price - (price * 0.1)

elif flower == "Dahlias":
    price = numflowers*3.80
    if numflowers > 90:
        price = price - (price*0.15)

elif flower == "Tulips":
    price = numflowers*2.80
    if numflowers > 80:
        price = price - (price*0.15)

elif flower == "Narcissus":
    price = numflowers*3.00
    if numflowers < 120:
        price = price + (price*0.15)

elif flower == "Gladiolus":
    price = numflowers*2.50
    if numflowers < 80:
        price = price +(price*0.2)

else:
    print("error")

diff = abs(budget - price)

if price>budget:
    print(f"Not enough money, you need {diff:.2f} leva more.")
else:
    print(f"Hey, you have a great garden with {numflowers} {flower} and {diff:.2f} leva left.")