# EVEN MORE SLOWER THAT PART 1 !

pos = []
fuels = []

def main():
    f = open("input.txt", "r")
    for x in f:
        pos = x.split(",")

    pos = list(map(int, pos))

    avg = int(round(sum(pos) / len(pos)))
    fuel = 0
    
    for i in range(0, max(pos)):
        avg = i
        print("{0} / {1}".format(avg ,max(pos)))
        for crab in pos:
            counter = 0
            while crab < avg:
                crab += 1
                fuel += 1 + counter
                counter += 1
            while crab > avg:
                crab -= 1
                fuel += 1 + counter
                counter += 1

        fuels.append(fuel)
        fuel = 0

    print(min(fuels))

if __name__ == "__main__":
    main()
