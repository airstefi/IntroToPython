price = float(input())
puzzle = int(input())
dolls = int(input())
teddy = int(input())
minions = int(input())
trucks = int(input())

toysprice = (puzzle*2.6) + (dolls * 3) + (teddy * 4.1) + (minions * 8.2) + (trucks*2)

totaltoys = puzzle + dolls + trucks + teddy +minions

if totaltoys >= 50:
    # discount = (25/100)*toysprice
    toysprice = toysprice - (toysprice*0.25)

toysprice = toysprice - (toysprice * 0.1)

leftover = abs(toysprice - price)
if toysprice >= price:
    print(f"Yes! {leftover:.2f} lv left.")
else:
    print(f"Not enough money! {leftover:.2f} lv needed.")

