def printBoard(board):
    pass
def safe_pos(board,roe,col):
    pass
def check(board,row):
    if row==n:
        printBoard(board)
    for col in range(0,n):
        if safe_pos(board,row,col)==True:
            board[row][col]=1
            check(board,row-1)
        board[row][col]=0
board=[[0,1,0,0],
       [0,0,0,1],
       [1,0,0,0],
       [0,0,1,0]]
n=len(board)
print(check(board,0))