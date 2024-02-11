fruit = input()
day = input()
num = float(input())
price = 0.0

if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
    if fruit == "banana":
        price = 2.5*num
        print(f"{price:.2f}")
    elif fruit == "apple":
        price = 1.2*num
        print(f"{price:.2f}")
    elif fruit == "orange":
        price = 0.85*num
        print(f"{price:.2f}")
    elif fruit == "grapefruit":
        price = 1.45*num
        print(f"{price:.2f}")
    elif fruit == "kiwi":
        price = 2.7*num
        print(f"{price:.2f}")
    elif fruit == "pineapple":
        price = 5.5*num
        print(f"{price:.2f}")
    elif fruit == "grapes":
        price = 3.85*num
        print(f"{price:.2f}")
    else:
        print("error")

elif day == "Saturday" or day == "Sunday":
    if fruit == "banana":
        price = 2.7*num
        print(f"{price:.2f}")
    elif fruit == "apple":
        price = 1.25*num
        print(f"{price:.2f}")
    elif fruit == "orange":
        price = 0.9*num
        print(f"{price:.2f}")
    elif fruit == "grapefruit":
        price = 1.6*num
        print(f"{price:.2f}")
    elif fruit == "kiwi":
        price = 3*num
        print(f"{price:.2f}")
    elif fruit == "pineapple":
        price = 5.6*num
        print(f"{price:.2f}")
    elif fruit == "grapes":
        price = 4.2*num
        print(f"{price:.2f}")
    else:
        print("error")
else:
    print("error")


