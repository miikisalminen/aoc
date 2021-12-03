# This solution actually does not work, ill have to come back to this

from collections import Counter

input_list = []
oxygen = ""
co2 = ""

# ls : list to search
# pos : bit position
# pref : preferred outcome of a equality
def findMostCommonBit(ls, pos, pref):
    ones = 0
    zeros = 0
    for i in ls:
        if(i[pos] == "0"):
            zeros+=1
        else:
            ones+=1
    
    if(ones > zeros):
        return "1"
    if(ones == zeros and pref == "1"):
        return "1"
    
    if(zeros > ones):
        return "0"
    if(zeros == ones and pref == "0"):
        return "0"

def calcOxygenRating(ls):
    while len(ls) != 1:
        for i in range(12):
            common = findMostCommonBit(ls, i, "1")
            for j in ls:
                if j[i] != common:
                    ls.remove(j)
    print("oxygen " + ls[0])
    return (int(ls[0], 2))

def calcCO2Scrubber(ls):
    while len(ls) != 1:
        for i in range(12):
            common = findMostCommonBit(ls, i, "0")
            for j in ls:
                if j[i] != common:
                    ls.remove(j)
    print(ls)
    return (int(ls[0], 2))

def main():
    f = open("input.txt", "r")
    for x in f:
        input_list.append(x.strip())
    
    print(calcCO2Scrubber(input_list.copy()) * calcOxygenRating(input_list.copy()) )

if __name__ == "__main__":
    main()


#print(oxygen + " : " + gamma)
#print(co2 + " : " + epsilon)
#print(int(oxygen, 2) * int(co2, 2))
