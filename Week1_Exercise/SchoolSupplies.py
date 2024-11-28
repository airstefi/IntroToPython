pen_num = int(input())
marker_num = int(input())
liter_chemical = int(input())
percent = int(input())

discount = percent/100

price_pen = pen_num*5.8
price_marker = marker_num * 7.2
chemical_price = liter_chemical * 1.2

total = price_marker + price_pen + chemical_price

total_discount = total - (total*discount)

print(total_discount)
