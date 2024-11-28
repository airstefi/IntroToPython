balance = 0

while True:
    data = input()
    if data == "NoMoreMoney":
        break

    if float(data) >= 0:
        print(f"Increase: {float(data):.2f}")
        balance = balance + float(data)
    else:
        print(f"Invalid operation!")
        break


print(f"Total: {balance:.2f}")


