product = input()
city = input()
num = float(input())

price = 0

if city == "Sofia":
    if product == "coffee":
        price = num * 0.5
    if product == "water":
        price = num * 0.8
    if product == "beer":
        price = num * 1.2
    if product == "sweets":
        price = num*1.45
    if product == "peanuts":
        price = num*1.6
elif city == "Plovdiv":
    if product == "coffee":
        price = num * 0.4
    if product == "water":
        price = num * 0.7
    if product == "beer":
        price = num * 1.15
    if product == "sweets":
        price = num*1.30
    if product == "peanuts":
        price = num*1.50
else:
    if product == "coffee":
        price = num * 0.45
    if product == "water":
        price = num * 0.7
    if product == "beer":
        price = num * 1.1
    if product == "sweets":
        price = num*1.35
    if product == "peanuts":
        price = num*1.55

print(price)