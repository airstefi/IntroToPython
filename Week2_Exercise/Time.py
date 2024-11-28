hour = int(input())
mins = int(input())

temp = 0;

if mins + 15 > 59:
    hour = hour + 1
    temp = mins + 15
    mins = temp - 60
    # if(hour == 0 ):
    #     hour = 24
else:
    mins = mins + 15

if mins < 10:
    print(f"{hour}:0{mins}")
else:
    print(f"{hour}:{mins}")
