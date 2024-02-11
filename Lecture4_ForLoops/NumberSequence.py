from sys import maxsize

pairs = int(input())

max = -maxsize
min = +maxsize

for numbers in range(pairs):
    current = int(input())

    if max < current:
        max = current

    if min > current:
        min = current


print(f"Max number: {max}")
print(f"Min number: {min}")