# Day 4: Giant Squid
# https://adventofcode.com/2021/day/4

class BingoBoard:
    def __init__(self, b):
        self.score = None
        self.is_won = False
        self.board = []
        self.marked = []
        for i in range(5):
            self.board.append([n for n in b[i]])
            self.marked.append([False for f in range(5)])
    
    def __str__(self):
        srep = ""
        for row in range(5):
            for col in range(5):
                srep += "{:3}".format(self.board[row][col])
            srep += "\n"
        return srep
    
    def mark(self, num):
        if self.is_won:
            return True
        for row in range(5):
            for col in range(5):
                if self.board[row][col] == num:
                    # mark number
                    self.marked[row][col] = True
                    # check if board wins
                    is_row_complited = True
                    is_col_complited = True
                    for k in range(5):
                        is_row_complited &= self.marked[row][k]
                        is_col_complited &= self.marked[k][col]
                    if is_row_complited or is_col_complited:
                        # calculate score
                        self.score = 0
                        for r in range(5):
                            for c in range(5):
                                if not self.marked[r][c]:
                                    self.score += self.board[r][c]
                        self.score *= num
                        self.is_won = True
                        return True
        return False


boards = []
with open("input.txt") as file:
    rand = [int(n) for n in file.readline().split(",")]
    line = file.readline()
    while line:
        board = []
        for i in range(5):
            board.append([int(n) for n in file.readline().split()])
        boards.append(BingoBoard(board))
        line = file.readline()
    
# print(rand)
print(f"Read {len(boards)} boards.")
# print(boards[0])

tally = 1
for rnum in rand:
    i = 1
    tally += 1
    for board in boards:
        i += 1
        if not board.is_won and board.mark(rnum):
            print(f"{tally}: Board #{i} wins at number {rnum}. Score is {board.score}.")

