num = float(input())

bonus = 0

if num < 100:
    bonus = 5
elif num > 1000:
    bonus = 0.1 * num
else:
    bonus = 0.2 * num

if num % 2 == 0:
    bonus = bonus +1
elif num%10 == 5:
    bonus = bonus +2
# elif num%100 == 5:
#     bonus = bonus+5


print(bonus)
print(bonus + num)
