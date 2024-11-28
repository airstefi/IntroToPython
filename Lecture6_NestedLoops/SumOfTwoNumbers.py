start = int(input())
end = int(input())
magicnum = int(input())

combination = 0
found = False

for i in range (start, end+1):
    for j in range(start, end+1):

        combination += 1

        if i + j == magicnum:
            print(f"Combination N:{combination} ({i} + {j} = {magicnum})")
            found = True
            break

    if found == True:
        break

else:
    print(f"{combination} combinations - neither equals {magicnum}")