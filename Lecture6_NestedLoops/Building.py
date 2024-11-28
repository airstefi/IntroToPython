floors = int(input())
rooms = int(input())


for i in reversed(range(1, floors+1)):
    room = "A" if i % 2 else "O"

    if i == floors:
        room = "L"

    for j in range(rooms):
        roomname = f"{room}{i}{j}"
        print(roomname, end=' ')

    print()