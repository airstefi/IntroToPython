import math
showname = input()
episode_time = int(input())
break_time = int(input())

lunch = break_time*(1/8)
rest = break_time*(1/4)

leftover = break_time - lunch - rest

diff = abs(leftover - episode_time)
rounded = math.ceil(diff)
if leftover >= episode_time:
    print(f"You have enough time to watch {showname} and left with {rounded} minutes free time.")
else:
    print(f"You don't have enough time to watch {showname}, you need {rounded} more minutes.")