month = input()
num = int(input())

studio = 0
apartament = 0


if month == "May" or month == "October":
    studio = 50
    apartament = 65
    if 7 <= num < 14:
        studio = studio - (studio * 0.05)
    elif num >= 14:
        studio = studio - (studio * 0.3)

elif month == "June" or month == "September":
    studio = 75.20
    apartament = 68.70
    if num >= 14:
        studio = studio - (studio * 0.2)

elif month == "July" or month == "August":
    studio = 76
    apartament = 77

else:
    print("error")


if num > 14:
    apartament = apartament-(apartament*0.1)

pricestudio = studio*num
priceapartment = apartament*num

print(f"Apartment: {priceapartment:.2f} lv.")
print(f"Studio: {pricestudio:.2f} lv.")



