n = int(input())

'''
Creates 8x8 board where an "empty" space is filled with 0
'''
board = [[0]*n for _ in range(n)]


def is_not_safe(row, col):
    '''
    Checks if there is a queen(represented by "1") in 
    in the adjacent row or column
    '''
    for i in range(0, n):
        if board[row][i]==1 or board[i][col]==1:
            return True
    '''
    Checks if there is a queen(represented by "1") in 
    in the diagonals
    '''
    for j in range(0, n):
        for k in range(0, n):
            if (j+k==row+col) or (j-k==row-col):
                if board[j][k]==1:
                    return True
    return False

def solve_n_queens(queen):
    # if count of queen is 0, then solution is found
    if queen==0:
        return True
    for row in range(0, n):
        for col in range(0, n):
            '''
            Checks if a queen can be placed in the position or not,
            a queen will not be placed if the position is not safe or
            if it is already occupied
            '''
            if (not(is_not_safe(row, col))) and (board[row][col] !=1 ):
                board[row][col] = 1
                #recursion part to check if we can put a queen in the current board
                if solve_n_queens(queen-1)==True:
                    return True
                board[row][col] = 0
    return False

#call the function to display solution
solve_n_queens(n)
for row in board:
    print (row)
