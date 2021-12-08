
segments = {}

# Matching output with the now-known segments
def check_output(set1, outputs):
    ans = ""
    for output in outputs:
        for key in set1:
            if set1[key] == string_into_set(output):
                ans += key 
    return int(ans)

# String into a set by char
def string_into_set(string):
    result_set = set()
    for char in string:
        result_set.update(char)
    return result_set

# Finds first element by length in array
def find_by_len(arr, length):
    
    result = set()

    for elem in arr:
        if len(elem) == length:
            result = string_into_set(elem)
    return result

# find by length and as a subset of a given segment
def find_by_len_subset(arr, length, set1):
    result = set()

    for elem in arr:
        if len(elem) == length and set1.issubset(string_into_set(elem)):
            return string_into_set(elem)


# Finds signal that is one longer and has an union of two signals as a subset
def find_one_longer_union(arr, set1, set2):
    union = set.union(set1, set2)
    for elem in arr:
        if len(elem) == len(union) + 1 and union.issubset(string_into_set(elem)):
            return string_into_set(elem)

def find_diff(arr, set1, set2):
    diff = set1.difference(set2)
    for elem in arr:
        if string_into_set(elem) == diff:
            return string_into_set(elem)

def find_one_longer_diff(arr, set1, set2):
    diff = set1.difference(set2)
    for elem in arr:
        if len(elem) == len(diff) + 1 and diff.issubset(string_into_set(elem)):
            return string_into_set(elem)

def main():
    output_sum = 0
    displays = []

    f = open("input.txt", "r")
    for i in f:
        displays.append([i.split("|")[0].strip().split(" "), i.split("|")[1].strip().split(" ")])    

    for display in displays:
        signals = display[0]
        outputs = display[1]

        # Matching all segments with simple union-difference operations
        segments['1'] = find_by_len(signals, 2)
        segments['4'] = find_by_len(signals, 4)
        segments['7'] = find_by_len(signals, 3)
        segments['8'] = find_by_len(signals, 7)
        segments['9'] = find_one_longer_union(signals, segments['4'], segments['7']) 
        segments['5'] = find_one_longer_diff(signals, segments['9'], segments['1'])
        segments['6'] = find_diff(signals, segments['8'], segments['9'].difference(segments['5']))
        segments['3'] = find_by_len_subset(signals, 5, segments['1'])
        segments['2'] = find_by_len_subset(signals, 5, segments['8'].difference(segments['5']))
        segments['0'] = find_by_len_subset(signals, 6, set.union(segments['8'].difference(segments['9']), segments['8'].difference(segments['6']))) 
        
        output_sum += check_output(segments, outputs)
    
    print(output_sum)






if __name__ == "__main__":
    main()
