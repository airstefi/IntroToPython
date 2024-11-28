tournaments = int(input())
points = int(input())
foravg = 0
wins = 0

for i in range(tournaments):
    phase = input()

    if phase == "W":
        points = points + 2000
        foravg = foravg + 2000
        wins = wins + 1

    elif phase == "F":
        points = points + 1200
        foravg = foravg + 1200
    else:
        points = points + 720
        foravg = foravg + 720

avg = int(foravg/tournaments)
winsaverage = (wins/tournaments)*100

print(f"Final points: {points:.0f}")
print(f"Average points: {avg}")
print(f"{winsaverage:.2f}%")


