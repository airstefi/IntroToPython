
steps = 0
total = 0

while True:
    user = input()

    if user == "Going home":
        stepshome = int(input())
        total = total + stepshome
        if total>= 10000:
            diff = total - 10000
            print(f"Goal reached! Good job!")
            print(f"{diff} steps over the goal!")
            break
        else:
            diff = 10000 - total
            print(f"{diff} more steps to reach goal.")
            break
    else:
        steps = int(user)

    total = total + steps

    if total >= 10000:
        diff = total - 10000
        print(f"Goal reached! Good job!")
        print(f"{diff} steps over the goal!")
        break



