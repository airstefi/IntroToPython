from math import pi

figure = input()

if figure == "square":
    side = float(input())
    area = side*side
    print(round(area,3))

elif figure =="rectangle":
    len1 = float(input())
    len2 = float(input())
    area = len1 * len2
    print(round(area,3))

elif figure == "circle":
    r = float(input())
    area = pi*(r*r)
    print(round(area,3))

else:
    base = float(input())
    h = float(input())
    area = (base*h)/2
    print(round(area,3))
