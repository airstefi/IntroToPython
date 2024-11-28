age = int(input())
washer = float(input())
toy = int(input())

savings = 0
count = 0
toysnum = 0

for i in range(1, age+1):

    if i%2 == 0:
        count = count + 1
        savings = savings + (10*count)

    else:
        toysnum = toysnum+1


toysmoney = toysnum * toy

totalsavings = (savings+toysmoney)-count

# print(savings)
# print(toysmoney)
# print(count)


diff = abs(totalsavings-washer)
if totalsavings > washer:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")