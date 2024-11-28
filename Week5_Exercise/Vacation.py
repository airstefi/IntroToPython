moneyneeded = float(input())
balance = float(input())

days = 0
spendingcount = 0


while True:
    action = input()
    amount = float(input())
    days = days+1

    if action == "spend":
        balance = balance - amount
        spendingcount = spendingcount + 1

        if balance <= 0:
            balance = 0

        if spendingcount >= 5:
            print(f"You can't save the money.")
            print(f"{spendingcount}")
            break


    else:
        balance = balance + amount
        spendingcount = 0

        if balance >= moneyneeded:
            print(f"You saved the money for {days} days.")
            break

