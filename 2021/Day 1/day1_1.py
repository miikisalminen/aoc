
prev = 0
count = 0

f = open("input.txt", "r")
for x in f:
    if(int(x.strip()) > prev):
        count = count + 1
    prev = int(x.strip())

print(count - 1)