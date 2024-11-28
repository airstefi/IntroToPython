browsernum = int(input())
salary = int(input())

for i in range(browsernum):
    name = input()

    if name == "Facebook":
        salary = salary - 150
    elif name == "Instagram":
        salary = salary - 100
    elif name == "Reddit":
        salary = salary - 50
    else:
        salary = salary

    if salary <= 0:
        print(f"You have lost your salary.")
        break

else:
    print(salary)