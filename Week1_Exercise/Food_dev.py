chicken = int(input())
fish = int(input())
vegetarian = int(input())

chicken_price = chicken*10.35
fish_price = fish*12.4
vegetarian_price = vegetarian*8.15

total_price = chicken_price+fish_price+vegetarian_price

dessert = (20/100)*total_price
delivery = 2.5

total = total_price + dessert+delivery

print(total)
