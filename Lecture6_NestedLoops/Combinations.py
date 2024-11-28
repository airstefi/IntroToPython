num = int(input())
count = 0

for i in range(0,num+1):
    for j in range(0,num+1):
        for k in range(0,num+1):
            if i+j+k==num:
                count = count+1

print(count)