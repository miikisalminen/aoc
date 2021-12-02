
horizontal = 0
vertical = 0

f = open("input.txt", "r")
for x in f:
    direction = x.split()[0]
    distance = int(x.split()[1].strip())
    
    if(direction == "forward"):
        horizontal = horizontal + distance
    elif(direction == "up"):
        vertical = vertical - distance
    elif(direction == "down"):
        vertical = vertical + distance

print(horizontal * vertical)