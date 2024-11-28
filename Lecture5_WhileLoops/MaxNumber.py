from sys import maxsize

max = -maxsize

while True:
    current = input()
    if current == "Stop":
        break

    if int(current) > max:
        max = int(current)



print(max)
