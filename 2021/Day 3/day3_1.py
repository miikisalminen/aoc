from collections import Counter

input_list = []
gamma = ""
epsilon = ""
tmp = ""

f = open("input.txt", "r")
for x in f:
    input_list.append(x.strip())

# Traversing list top-down
for i in  range(len(input_list[0])):
    for j in range(len(input_list)): 
        tmp+=input_list[j][i]
    # Finding most frequent char
    res = Counter(tmp)
    res = max(res, key=res.get)
    
    gamma+=str(res)
    epsilon+=str(1 - int(res))
    tmp=""
# Conversion to decimal
print(int(gamma, 2) * int(epsilon, 2))