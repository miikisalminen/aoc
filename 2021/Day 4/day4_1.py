input_list = []
drawn = []
rows = []
cols = []

# what boards rows are a part of: //5
# what boards cols are a part of: +100

def check_rows(ball_num):
    for i in range(len(rows)):
        for j in range(len(rows[i])):
            if rows[i][j] == ball_num:
                rows[i][j] = "X"
    if ["X","X","X","X","X"] in rows:
        #print("WINNING ROW:")
        #print(rows.index(["X","X","X","X","X"])//5)
        return rows.index(["X","X","X","X","X"])
    else:
        return -1

def check_cols(ball_num):
    for i in range(len(cols)):
        for j in range(len(cols[i])):
            if cols[i][j] == ball_num:
                cols[i][j] = "X"
    if ["X","X","X","X","X"] in cols:
        print("WINNING COLUMN:")
        print(cols.index(["X","X","X","X","X"]))
        return True
    else:
        return False

def main():
    f = open("input.txt", "r")
    for x in f:
        if x.strip() != "":
            input_list.append(x.strip())
    
    drawn = input_list[0].split(",")

    for i in range(1, len(input_list)):
        rows.append(input_list[i].split())
    tmp = []
    for i in range(5):
        for j in range(len(rows)):
            tmp.append(rows[j][i])
            if len(tmp) == 5:
                cols.append(tmp)
                tmp = []
                continue
        

    # Drawing all numbers
    while(len(drawn) > 0):
        last_drawn = drawn[0]
        winning_board = check_rows(last_drawn)
        if winning_board != -1:
            print("the winning board is #" + str(winning_board))
            break
        drawn.pop(0)
    for i in range(winning_board-5, winning_board+5):
        print(rows[i])
    print(last_drawn)

if __name__ == "__main__":
    main()
