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
		if numCnt[i] == grid_dim:
			nComplete[i] = True

	return emptyCnt


# Verifies that the puzzle has the correct format:
#   "Each number occurs once per column, row, and block
# Returns True if the puzzle is consistent
def verify_puzzle ( puz ):

	solved = True
	inconsistent = False
	# For each row or column
	for i in np.arange(grid_dim):
		ccols = np.zeros((grid_dim), dtype=int)
		crows = np.zeros((grid_dim), dtype=int)

		# For each cell in that row/column
		for j in np.arange(grid_dim):

			# If the cell value is 0 keep checking for inconsistencies
			# Otherwise, increment the count of the r/c value

			# Row
			if puz[i][j] == 0:
				solved = False
			else:
				ccols[puz[i][j]-1] += 1

			# Column
			if puz[j][i] == 0:
				solved = False
			else:
				crows[puz[j][i]-1] += 1

		# The puzzle is inconsistent any r/c has more than one of a single value
		if (ccols >= 2).any() or (crows >= 2).any():
			inconsistent = True
			solved = False
			break
		# The puzzle is not solved if every value is not contained in each r/c
		elif not ((ccols == 1).all() and (crows == 1).all()):
			solved = False

	# If no inconsistencies have been found
	if not inconsistent:
		# Count the multiplicity of each number in each cell of each block
		for i in np.arange(0,grid_dim,block_dim):
			for j in np.arange(0,grid_dim,block_dim):
				cblocks = np.zeros((grid_dim), dtype=int)
				for ik in np.arange(block_dim):
					for jk in np.arange(block_dim):
						x = i + ik
						y = j + jk

						# If the cell value is 0 keep checking for inconsistencies
						if puz[x][y] == 0:
							solved = False
							continue
						# Otherwise increment the count of the block value
						else:
							cblocks[puz[x][y]-1] += 1

				# The puzzle is inconsistent if a block contains more than one of a single value
				if (cblocks >= 2).any():
					inconsistent = True
					solved = False
					break
				# The puzzle is not solved if every value is not contained in each block
				elif not (cblocks == 1).all():
					solved = False

	# Alert the user if the puzzle is inconsistent
	if inconsistent:
		print('Inconsistent Puzzle')

	return solved