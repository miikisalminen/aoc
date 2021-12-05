ocean_map = []

# Making ocean_map
for i in range(1000):
    tmp = []
    for j in range(1000):
        tmp.append(0)
    ocean_map.append(tmp)
    tmp = []


def draw_line(line):
    # Indentify and draw vertical line
    if line[0][0] == line[1][0]:
        if line[0][1] > line[1][1]:
            for i in range(line[0][1], line[1][1]-1, -1):
                ocean_map[i][line[0][0]] += 1
        else:
            for i in range(line[0][1], line[1][1]+1):
                ocean_map[i][line[0][0]] += 1
    
    # Indentify and draw horizontal line
    elif line[0][1] == line[1][1]:
        if line[0][0] > line[1][0]:
            for i in range(line[0][0], line[1][0]-1, -1):
                ocean_map[line[0][1]][i] += 1
        else:
            for i in range(line[0][0], line[1][0]+1):
                ocean_map[line[0][1]][i] += 1

    # If not vertical / horizontal, must be diagonal
    else:
        y = line[0][1]
        # If x1 > x2...
        if line[0][0] > line[1][0]:
            # If y1 > y2
            if line[0][1] > line[1][1]:
                # 🡿
                for x in range(line[0][0], line[1][0]-1, -1):
                    ocean_map[y][x] += 1
                    y -= 1
            else:
                # 🡾
                for x in range(line[0][0], line[1][0]-1, -1):
                    ocean_map[y][x] += 1
                    y += 1
        else:
            # If y1 > y2
            if line[0][1] > line[1][1]:
                # 🢄
                for x in range(line[0][0], line[1][0]+1):
                    ocean_map[y][x] += 1
                    y -= 1
            else:
                # 🢅
                for x in range(line[0][0], line[1][0]+1):
                    ocean_map[y][x] += 1
                    y += 1



# Calculating ocean_map points
def calc_points():
    counter = 0
    for row in ocean_map:
        for num in row:
            if num >= 2:
                counter += 1
    print("Part 2 points: " + str(counter))

def main():
    # Reading in the lines into a list of lists of 2 tuples
    lines = []
    tmp = []
    f = open("input.txt", "r")
    for x in f:
        for y in x.strip().split(" -> "):
            tmp.append((int(y.split(",")[0]),int(y.split(",")[1])))
            if len(tmp) == 2:
                lines.append(tmp)
                tmp = []
    
    for line in lines:
        draw_line(line)

    calc_points()
if __name__ == "__main__":
    main()
