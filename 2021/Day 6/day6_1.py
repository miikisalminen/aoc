# Simple simple simple.....

fishes = []

def main():
    f = open("input.txt", "r")
    for x in f:
        fishes = x.split(",")
    
    fishes = list(map(int, fishes))
    print(fishes)

    for day in range(0,81):
        print("DAY {0}: {1} fishes roam about!".format(day, len(fishes)))
        for i in range(len(fishes)):
            if fishes[i] == 0:
                fishes.append(8)
                fishes[i] = 6
            else:
                fishes[i] -= 1
       

if __name__ == "__main__":
    main()
