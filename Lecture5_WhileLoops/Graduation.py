name = input()

gradecounter = 0

fail = 0
total = 0.0

while True:
    grade = float(input()) #grade for the year

    if grade<4:
        fail = fail + 1
        if fail >= 2:
            gradecounter = gradecounter + 1
            print(f"{name} has been excluded at {gradecounter} grade")
            break
        continue

    else:
        gradecounter = gradecounter + 1
        total = total + grade  # getting the sum of all the grades

    if gradecounter == 12:
        final = total / gradecounter
        print(f"{name} graduated. Average grade: {final:.2f}")
        break

# if fail>=2:
#     print(f"{name} has been excluded at {gradecounter} grade")
# else:
#