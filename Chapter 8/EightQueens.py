# Eight Queens: Write an algorithm to print all ways of arranging eight queens on an 8x8 chess board
# so that none of them share the same row, column, or diagonal. In this case, "diagonal" means all
# diagonals, not just the two that bisect the board.

# Generalizing to N Queens

def n_queens(n: int):
    cols = set()
    pos_diags = set()
    neg_diags = set()

    res = []
    board = [["."]*n for i in range(n)]

    def backtrack(r):
        if r == n:
            copy = ["".join(row) for row in board]
            res.append(copy)
            return
        for c in range(n):
            if c in cols or (r+c) in pos_diags or (r-c) in neg_diags: #for each diag, its row+col value is constant
                continue
            cols.add(c)
            pos_diags.add(r+c)
            neg_diags.add(r-c)
            board[r][c] = 'Q'
            
            backtrack(r+1)

            cols.remove(c)
            pos_diags.remove(r+c)
            neg_diags.remove(r-c)
            board[r][c] = "."
    backtrack(0)
    return res


n = 8

results = n_queens(n)

for result in results:
    for row in result:
        print(row)
    print("*******--------*******")