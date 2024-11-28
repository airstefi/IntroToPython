import math
record = float(input())
distance = float(input())
time = float(input()) #time to swim 1 meter

time_needed = distance * time
time_added = math.floor(distance/15)*12.5


total_time = time_needed+time_added

diff = abs(record - total_time)

if record<=total_time:
    print(f"No, he failed! He was {diff:.2f} seconds slower.")
else:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")