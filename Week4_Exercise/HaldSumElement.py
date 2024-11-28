from sys import maxsize

num = int(input())

max = -maxsize
sum = 0

for i in range(num):
    current = int(input())
    sum = sum + current

    if max < current:
        max = current


sum = sum - max

if max == sum:
    print(f"Yes")
    print(f"Sum = {sum}")
else:
    diff = abs(sum - max)
    print(f"No")
    print(f"Diff = {diff}")