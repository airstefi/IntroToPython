plastic = int(input())
paint = int(input())
mixer = int(input())
hours = int(input())

plastic_price = (plastic+2)*1.5
paint_price = (paint*1.1)*14.5
# print(paint_price)
mixer_price = mixer*5
bags = 0.4

total_price = plastic_price+paint_price+mixer_price+bags
# print(total_price)
price_workers = (total_price*0.3)*hours

total = total_price+price_workers

print(total)