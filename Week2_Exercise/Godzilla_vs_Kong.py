budget = float(input())
s = int(input())
clothing = float(input())

director = budget*0.1

# print(director)

#the cost of the clothing for everyone
sum_clothing = clothing * s

if s > 150:
    sum_clothing = sum_clothing - (sum_clothing * 0.1)

total = director + sum_clothing
# print(total)

diff = abs(budget - total)

# diff = round(diff,2)

# print(diff)

if budget>=total:
    print(f"Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")
else:
    print(f"Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")