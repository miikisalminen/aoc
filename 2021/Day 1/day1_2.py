
input_ = []
prev = 0
count = 0

f = open("input.txt", "r")
for x in f:
    input_.append(int(x.strip()))

for i in range(len(input_)):
    try:
        sum_ = input_[i] + input_[i+1] + input_[i+2] 
    except IndexError:
        break        
    if(sum_ > prev):
        count = count + 1
    prev = sum_


print(count - 1)