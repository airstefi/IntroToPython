length = int(input())
width = int(input())
height = int(input())
percent = float(input())

volume = length*width*height
volumeliters = volume/1000
space = percent/100
litersneeded = volumeliters*(1-space)

print(litersneeded)