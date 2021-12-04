
def find_most_common(ls, pos):
    ones = 0
    zeros = 0

    for i in ls:
        if(i[pos] == "0"):
            zeros = zeros + 1
        if(i[pos] == "1"):
            ones = ones + 1

    if(ones >= zeros):
        return "1"
    else:
        return "0"

def find_least_common(ls, pos):
    ones = 0
    zeros = 0

    for i in ls:
        if(i[pos] == "0"):
            zeros = zeros + 1
        if(i[pos] == "1"):
            ones = ones + 1
    
    if(ones >= zeros):
        return "0"
    else:
        return "1"

def convert(bin):
    return int(bin, 2)

def oxygen_rating(ls):
    e = 0
    while e < len(ls):
        for i in range(12):
            for j in range(len(ls)):
                try:
                    if ls[j][i] != find_most_common(ls, i):
                        del ls[j]
                        e = e + 1
                except IndexError:
                    continue
                
    return ls

def scrubber_rating(ls):
    e = 0
    while e < len(ls):
        for i in range(12):
            for j in range(len(ls)):
                try:
                    if ls[j][i] != find_least_common(ls, i):
                        del ls[j]
                        e = e + 1
                except IndexError:
                    continue
                
    return ls

def main():
    input_list = []
    f = open("input.txt", "r")
    for x in f:
        input_list.append(x.strip())
    
    oxygen_list = input_list.copy()
    scrubber_list = input_list.copy()

    oxygen_list = oxygen_rating(oxygen_list)
    print(oxygen_list)

    scrubber_list = scrubber_rating(scrubber_list)
    print(scrubber_list)

    print(convert(oxygen_list[3]) * convert(scrubber_list[3]) )

if __name__ == "__main__":
    main()
