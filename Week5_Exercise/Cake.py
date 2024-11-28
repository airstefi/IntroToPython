width = int(input())
length = int(input())

pieces = width * length

while True:
    i = input()

    if i == "STOP":
        print(f"{pieces} pieces are left.")
        break

    taken = int(i)

    pieces = pieces - taken

    if pieces <= 0:
        diff = abs(pieces)
        print(f"No more cake left! You need {diff} pieces more.")
        break



