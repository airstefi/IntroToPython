num = int(input())

sum1 = 0
sum2 = 0

index = 2*num

for i in range(index//2):
    current = int(input())
    sum1 = sum1 + current

for y in range(index//2):
    current = int(input())
    sum2 = sum2 + current


if sum1 == sum2:
    print(f"Yes, sum = {sum1}")
else:
    diff = abs(sum1-sum2)
    print(f"No, diff = {diff}")