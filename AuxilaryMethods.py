import numpy as np
from Puzzles import *
from SolveMethods import *

# Print Sudoku in a readable format
def display_puzzle ( puz ):
	output = '\n'
	for i in np.arange(grid_dim+2):
		# Pretty spacings
		if i == 3 or i == 7:
			output += ('-'*(2*grid_dim+3)) + '\n'
			continue
		
		# Correct indices for pretty spacings
		if i > 7:
			i -= 2
		elif i > 3:
			i -= 1
			
		for j in np.arange(grid_dim+2):
			# Pretty spacings
			if j == 3 or j == 7:
				output += '| '
				continue
				
			# Correct indices for pretty spacings
			if j > 7:
				j -= 2
			elif j > 3:
				j -= 1

			# Append number
			if puz[i][j] == 0:
				output += '* '
			else:
				output += '%d '%puz[i][j]

		# Add carrige return
		output = output[:-1]+'\n'
	print(output)

# Updates boolean values in nComplete to reflect the state of the Sudoku puzzle
# Returns the number of unsolved cells
def find_completed_numbers ( puz, nComplete ):
	numCnt = np.zeros((grid_dim), dtype=int)
	emptyCnt = 0

	# Count numbers
	for i in np.arange(grid_dim):
		for j in np.arange(grid_dim):
			if puz[i][j] != 0:
				numCnt[puz[i][j]-1] += 1
			else:
				emptyCnt += 1

	# Find completed numbers
	for i in np.arange(grid_dim):
		if numCnt[i] == 9:
			nComplete[i] = True

	return emptyCnt

# Verifies that the puzzle has the correct format:
#   "Each number occurs once per column, row, and block
# Returns True if the puzzle is consistent
def verify_puzzle ( puz ):

	# For each number in Sudoku
	for n in np.arange(1,grid_dim+1,1):
		# Check Columns and Rows
		for i in np.arange(grid_dim):
			rhasn, _ = row_contains_num(puz, i, n)
			chasn, _ = col_contains_num(puz, i, n)
			if not (rhasn and chasn):
				return False

		# Check each block in Sudoku
		for i in np.arange(0, grid_dim, block_dim):
			for j in np.arange(0, grid_dim, block_dim):
				if not block_contains_num(puz, i, j, n):
					return False
	
	return True