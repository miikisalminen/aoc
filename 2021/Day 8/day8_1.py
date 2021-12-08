
def main():
    uniques = 0
    f = open("input.txt", "r")
    for i in f:
        for j in i.split("|")[1].split():
            if len(j) == 2 or len(j) == 4 or len(j) == 3 or len(j) == 7:
                print(j)
                uniques += 1
    
    print(uniques)


if __name__ == "__main__":
    main()
