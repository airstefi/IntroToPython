num1 = int(input())
num2 = int(input())
operation = input()

total = 0

oddeven = ""

if operation == "+":
    total = num1+num2
    if total % 2 == 0:
        oddeven = "even"
    else:
        oddeven = "odd"

    print(f"{num1} + {num2} = {total} - {oddeven}")

elif operation == "-":
    total = num1-num2
    if total % 2 == 0:
        oddeven = "even"
    else:
        oddeven = "odd"

    print(f"{num1} - {num2} = {total} - {oddeven}")

elif operation == "*":
    total = num1*num2
    if total % 2 == 0:
        oddeven = "even"
    else:
        oddeven = "odd"

    print(f"{num1} * {num2} = {total} - {oddeven}")

elif operation == "/":
    if num2 == 0:
        print(f"Cannot divide {num1} by zero")
    else:
        total = num1/num2
        total = round(total, 2)
        print(f"{num1} / {num2} = {total}")

elif operation == "%":
    if num2 == 0:
        print(f"Cannot divide {num1} by zero")
    else:
        total = num1 % num2
        total = round(total, 2)
        print(f"{num1} % {num2} = {total}")

