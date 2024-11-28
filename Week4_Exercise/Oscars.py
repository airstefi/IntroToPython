actor = input()
academypoints = float(input())
jury = int(input())


for i in range(jury):
    juryname = input()
    points = float(input())
    num = len(juryname)

    academypoints = academypoints + ((num*points)/2)

    if academypoints > 1250.5:
        print(f"Congratulations, {actor} got a nominee for leading role with {academypoints:.1f}!")
        break
else:
    diff = abs(1250.5 - academypoints)
    print(f"Sorry, {actor} you need {diff:.1f} more!")