favbook = input()

checked = 0

while True:
    currentbook = input()

    if currentbook == favbook:
        print(f"You checked {checked} books and found it.")
        break
    if currentbook == "No More Books":
        print(f"The book you search is not here!")
        print(f"You checked {checked} books.")
        break

    checked = checked + 1