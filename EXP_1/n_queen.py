global N 
N = 4

def checkSafe(board, row, col): 
	# STEP 1 row left side
	for i in range(col): 
		if board[row][i] == 1: 
			return False
	# upper diagonal left side 
	for i, j in zip(range(row, -1, -1), range(col, -1, -1)): 
		if board[i][j] == 1: 
			return False

	# lower diagonal left side 
	for i, j in zip(range(row, N, 1), range(col, -1, -1)): 
		if board[i][j] == 1: 
			return False
    #default yes 
	return True

def solveNQueen(board, col): 
	# STEP 1(a) if all queens are placed 
	if col >= N: 
		return True

	# placing this queen in all rows one by one 
	for i in range(N): 
        #STEP 2(a) Check if can be placed safely
		if checkSafe(board, i, col):
			board[i][col] = 1
			if solveNQueen(board, col + 1) == True: 
                #STEP 2(b) if placed, return true
				return True
			board[i][col] = 0
    #STEP 1(b) default, if queen not placed
	return False

def solveNQueenProblem(board): 
	if solveNQueen(board, 0) == False: 
		print ("Solution does not exist")
		return False
    # Print the solution
	for i in range(N): 
		for j in range(N): 
			print (board[i][j], end=" ")
		print("")
	return True


board = [ [0, 0, 0,0],[0, 0, 0,0], [0, 0, 0,0],[0, 0, 0,0]] #initialize the board

solveNQueenProblem(board) 



# ALGORITM-------------------------------------------------------------------------------------------------------
# 1. Start in the leftmost column
#    a) If all queens are placed
#       return true
#    b) Else
#       return false
# 2. Try all rows in the current column. 
#    Do following for every tried row.
#     a) If the queen can be placed safely in this row then mark this [row, column] as part of the 
#        solution and recursively check if placing queen here leads to a solution.
#     b) If placing the queen in [row, column] leads to a solution then return true.
#     c) If placing queen doesn't lead to a solution then  unmark this [row, column] (Backtrack) and go to 
#        step (a) to try other rows.
# 3. If all rows have been tried and nothing worked,
#    return false to trigger backtracking.



# Objective--------------------------------------------------------------------------
# The idea is to place queens one by one in different columns, 
# starting from the leftmost column. When we place a queen in a column,
#  we check for clashes with already placed queens. In the current column, 
#  if we find a row for which there is no clash, we mark this row and column 
#  as part of the solution. If we do not find such a row due to clashes 
#  then we backtrack and return false.