deposit_sum = float(input())
month = float(input())
percent = float(input())

p = percent/100
natural = deposit_sum*p

one_month = natural/12

total = deposit_sum+(month*one_month)

print(total)
