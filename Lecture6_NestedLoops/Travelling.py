balance = 0.0

while True:
    country = input()

    if country == "End":
        break

    budget = float(input())

    while True:
        savings = float(input())
        balance = savings + balance

        if balance >= budget:
            print(f"Going to {country}!")
            break

    balance = 0.0