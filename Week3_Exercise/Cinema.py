ticket = input()
rows = int(input())
columns = int(input())

income = 0;

capacity = rows*columns

if ticket == "Premiere":
    income = capacity * 12.00
elif ticket == "Normal":
    income = capacity * 7.50
elif ticket == "Discount":
    income = capacity * 5
else:
    print("error")


print(f"{income:.2f} leva")