time = int(input())
mins = int(input())
arrival_hour = int(input())
arrival_mins = int(input())

exam_in_mins = (time*60)+mins
arrival_in_mins = (arrival_hour*60)+arrival_mins

diffmin = 0
diffhour = 0

diff = abs(arrival_in_mins - exam_in_mins)

#hes late
if arrival_in_mins > exam_in_mins:
    print(f"Late")
    if diff>=60:
        diffhour = diff//60
        diffmin = diff % 60
        print(f"{diffhour}:{diffmin:02d} hours after the start")

    else:
        print(f"{diff} minutes after the start")

elif arrival_in_mins == exam_in_mins or diff<=30:
    print("On time")
    print(f"{diff} minutes before the start")

else:
    print("Early")
    if diff>=60:
        diffhour = diff//60
        diffmin = diff % 60
        print(f"{diffhour}:{diffmin:02d} hours before the start")

    else:
        print(f"{diff} minutes before the start")
