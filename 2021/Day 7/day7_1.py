# Very slow... very very very slow

pos = []
fuels = []

def main():
    f = open("input.txt", "r")
    for x in f:
        pos = x.split(",")

    pos = list(map(int, pos))

    avg = int(round(sum(pos) / len(pos)))
    fuel = 0
    
    for i in pos:
        avg = i
        for crab in pos:
            while crab < avg:
                crab += 1
                fuel += 1
            while crab > avg:
                crab -= 1
                fuel += 1
        fuels.append(fuel)
        fuel = 0

    print(min(fuels))

if __name__ == "__main__":
    main()
