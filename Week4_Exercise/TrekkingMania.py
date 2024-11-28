groupnum = int(input())

sumall = 0
musala = 0
monblan = 0
k = 0
k2 = 0
everest = 0

for i in range(groupnum):
    smallgroup = int(input())

    if smallgroup <= 5:
        musala = musala + smallgroup

    elif 6<= smallgroup<=12:
        monblan = monblan + smallgroup

    elif 13<=smallgroup<=25:
        k = k + smallgroup

    elif 26 <= smallgroup <=40:
        k2 = k2 + smallgroup

    else:
        everest = everest + smallgroup


sumall = musala + monblan + k + k2 + everest

musala = (musala/sumall)*100
monblan = (monblan/sumall)*100
k = (k/sumall)*100
k2 = (k2/sumall)*100
everest = (everest/sumall)*100

print(f"{musala:.2f}%")
print(f"{monblan:.2f}%")
print(f"{k:.2f}%")
print(f"{k2:.2f}%")
print(f"{everest:.2f}%")