import numpy as np
from Puzzles import *

# Replace location (x, y) in the puzzle with n
def place_n ( puz, x, y, n ):
	puz[x][y] = n
	if verbose:
		print('Placing %d at (%d,%d)'%(n, x, y))

# Returns True if row contains n
def row_contains_num ( puz, row, n ):
	for i in np.arange(grid_dim):
		if puz[row][i] == n:
			return True, i
	return False, -1

# Returns True if col contains n
def col_contains_num ( puz, col, n ):
	for i in np.arange(grid_dim):
		if puz[i][col] == n:
			return True, i
	return False, -1

# Returns True if the block_dim*block_dim grid starting at (row, col) contains n
def block_contains_num ( puz, row, col, n ):
	for i in np.arange(block_dim):
		for j in np.arange(block_dim):
			if puz[row+i][col+j] == n:
				return True
	return False

# Searches for definite numbers by checking cells within a block
#  mm is a matrix which remembers the possible values a cell can contain
def inner_block_method ( puz, n, mm ):
	# For each block
	for i in np.arange(0, grid_dim, block_dim):
		for j in np.arange(0, grid_dim, block_dim):

			# If the block does not contain n
			if not block_contains_num(puz, i, j, n):
				
				pcnt = 0
				ppos = None
				# Count the number of spots that n could possibly take
				for ik in np.arange(block_dim):
					for jk in np.arange(block_dim):
						x = i + ik
						y = j + jk
						# If the cell is available...
						if puz[x][y] == 0:
							# ...and that row and column are devoid of n
							#    increase the count and save the location
							rhasn, rp = row_contains_num(puz, x, n)
							chasn, cp = col_contains_num(puz, y, n)
							if not (rhasn or chasn):
								# Store n in memory matrix
								mm[x][y].append(n)
								pcnt += 1
								ppos = np.array([x, y])

				# If there is only one free space in this block place n in that spot.
				if pcnt == 1:
					place_n(puz, ppos[0], ppos[1], n)

# Searches for definite numbers in all rows or all columns
#  horiz == True   => Search Rows
#  horiz == False  => Search Columns
def line_method ( puz, horiz, n ):

	# For each line
	for i in np.arange(grid_dim):

		# Check for n in row or column
		if horiz:
			hasn, _ = row_contains_num(puz, i, n)
		else:
			hasn, _ = col_contains_num(puz, i, n)

		# Continue if row/column contains n
		if hasn:
			continue

		pcnt = 0
		ppos = -1
		# Count free cells in r/c
		for rc in np.arange(0, grid_dim, block_dim):

			# Set indices for block
			if horiz:
				x = 3*(i//block_dim)
				y = rc
			else:
				x = rc
				y = 3*(i//block_dim)

			# If the block doesn't contain n
			if not block_contains_num(puz, x, y, n):

				# Count free cells in block
				for rc2 in np.arange(block_dim):

					# Set indices for cell
					if horiz:
						x = i
						y = rc+rc2
					else:
						x = rc+rc2
						y = i

					# If cell is available
					if puz[x][y] == 0:

						# Check for n in r/c
						if horiz:
							hasn, _ = col_contains_num(puz, y, n)
						else:
							hasn, _ = row_contains_num(puz, x, n)

						# Increase count if r/c doesn't contain n
						if not hasn:
							pcnt += 1
							ppos = [x, y]

		# If count is one place n and return
		if pcnt == 1:
			place_n(puz, ppos[0], ppos[1], n)
			return
			
# Search the memory matrix for cells with only one possibility.
# mm is a memory matrix containing possibilities for each cell.
def memory_method ( puz, mm ):
	fchange = False
	# For each cell
	for i in np.arange(grid_dim):
		for j in np.arange(grid_dim):

			# If the cell has only one possibility for a solution
			if len(mm[i][j]) == 1:
				n = mm[i][j][0]
				rhasn, _ = row_contains_num(puz, i, n)
				chasn, _ = col_contains_num(puz, j, n)
				bhasn = block_contains_num(puz, i//block_dim, j//block_dim, n)

				# Make the change if this possibility is still valid
				if not (rhasn or chasn or bhasn):
					fchange = True
					place_n(puz, i, j, n)
	return fchange