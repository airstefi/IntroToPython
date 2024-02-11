pair = int(input())

odd = 0
even = 0

for i in range(pair):
    current = int(input())

    if i % 2 == 1:
        odd = odd + current

    if i % 2 == 0:
        even = even + current


if even == odd:
    print(f"Yes")
    print(f"Sum = {even}")
else:
    diff = abs(even - odd)
    print("No")
    print(f"Diff = {diff}")