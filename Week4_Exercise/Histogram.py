num = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for i in range(num):
    current = int(input())

    if current < 200:
        p1 = p1 + 1

    elif 200 <= current <= 399:
        p2 = p2 + 1
    elif 400<= current <= 599:
        p3 = p3+1
    elif 600<= current <= 799:
        p4 = p4 + 1
    else:
        p5 = p5 + 1

p1sum = (p1/num)*100
p2sum = (p2/num)*100
p3sum = (p3/num)*100
p4sum = (p4/num)*100
p5sum = (p5/num)*100

print(f"{p1sum:.2f}%")
print(f"{p2sum:.2f}%")
print(f"{p3sum:.2f}%")
print(f"{p4sum:.2f}%")
print(f"{p5sum:.2f}%")