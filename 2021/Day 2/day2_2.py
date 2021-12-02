
horizontal = 0
vertical = 0
aim = 0

f = open("input.txt", "r")
for x in f:
    direction = x.split()[0]
    distance = int(x.split()[1].strip())
    
    if(direction == "forward"):
        horizontal = horizontal + distance
        vertical = vertical + (distance * aim)
    elif(direction == "up"):
        aim = aim - distance
    elif(direction == "down"):
        aim = aim + distance

print(horizontal * vertical)