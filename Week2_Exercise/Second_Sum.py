import math
first = int(input())
second = int(input())
third = int(input())

total = first+second+third

mins = total/60
seconds = total%60

mins = math.floor(mins)

if seconds < 10:
    print(f"{mins}:0{seconds}")
else:
    print(f"{mins}:{seconds}")