from sys import maxsize

min = maxsize

while True:
    current = input()
    if current == "Stop":
        break

    if int(current) < min:
        min = int(current)



print(min)
