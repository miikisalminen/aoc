input_list = []
drawn = []
boards = []
# Array to keep track of order of winning bingo cards
winners = []

# Marks every boards num if they have it, then checks for winners.
# If a winner is found, the winning board is returned
# Otherwise return -1
def check_boards(num):

    # Write out marked number
    for i in range(len(boards)):
        for j in range(len(boards[i])):
            for k in range(len(boards[i][j])):
                if boards[i][j][k] == num and boards[i] not in winners:
                    boards[i][j][k] = "X"
    
    # Check for completed rows (add the cards to winners)
    for i in range(len(boards)):
        for j in range(len(boards[i])):
            if ["X","X","X","X","X"] in boards[i] and boards[i] not in winners:
                winners.append(boards[i])

    # Check for completed columns (add the cards to winners)
    for i in range(len(boards)):
        for j in range(5):
            if [row[j] for row in boards[i]] == ["X","X","X","X","X"] and boards[i] not in winners:
                winners.append(boards[i])
        
# Calculates score of board given
def calc_score(board, last_drawn):
    score = 0
    for row in board:
        for num in row:
            if num != "X":
                score = score + int(num)
    
    print("Part 2 score: {0}".format(score*int(last_drawn)))

def main():
    f = open("input.txt", "r")
    for x in f:
        if x.strip() != "":
            input_list.append(x.strip())

    # Creating a stack of the drawing numbers    
    drawn = input_list[0].split(",")

    # Filling boards[]
    tmp = []
    for i in range(1, len(input_list)):
        tmp.append(input_list[i].split())
        if len(tmp) == 5:
            boards.append(tmp)
            tmp = []
   
    # Drawing all numbers until every board has won
    while(len(drawn) > 0):
        last_drawn = drawn[0]
        check_boards(last_drawn)
        if len(winners) == len(boards):
            break
        drawn.pop(0)

    # Calculate score of the last index in winners, i.e the bingo card that finishes last.
    calc_score(winners[len(winners)-1], last_drawn)

if __name__ == "__main__":
    main()
