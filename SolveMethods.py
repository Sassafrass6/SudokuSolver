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
				return True, (row+i, col+i)
	return False

# Searches for definite numbers by checking cells within a block
def inner_block_method ( puz, n ):
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

# Faster method of searching for n when rows or columns of entire blocks contain two n's
#  horiz == True   => Search Rows of Blocks
#  horiz == False  => Search Columns of Blocks
def outer_block_method ( puz, horiz, n ):
	# For each r/c
	for i in np.arange(0, grid_dim, block_dim):

		# Array of bools representing whether block n is in a column
		parr = np.zeros((block_dim), dtype=bool)
		
		# An array storing the positions of located numbers
		narr = np.zeros((block_dim), dtype=int)

		ccnt = 0
		ppos = pblock = None
		hasn = pos = None
		# Iterate over the blocks and store column info
		for j in np.arange(block_dim):
			
			# Check r/c for n
			if horiz:
				hasn, pos = row_contains_num(puz, i+j, n)
			else:	
				hasn, pos = col_contains_num(puz, i+j, n)

			# If the row contains n increse count and save location
			if hasn:
				ccnt += 1
				parr[j] = True
				narr[j] = pos
			else:
				narr[j] = -1

		ppos = pblock = None
		
		# Array storing which blocks contain n
		warr = np.zeros((block_dim), dtype=bool)
		
		# If there are exactly two of three n's in a r/c of blocks
		if ccnt == 2:
			# Find the r/c not containing n
			for p in np.arange(block_dim):
				if parr[p] == False:
					ppos = p
				else:
					warr[narr[p]//block_dim] = True

			wcnt = 0
			wpos = -1
			# Find the index of this block
			for w in np.arange(block_dim):
				if not warr[w]:
					wcnt += 1
					wpos = w*block_dim
			
			fcnt = 0
			findex = -1
			# Count free cells in this row of the empty block
			for p in np.arange(block_dim):
				
				# Check r/c for n
				if horiz:
					hasn, _ = col_contains_num(puz, wpos+p, n)
				else:
					hasn, _ = row_contains_num(puz, wpos+p, n)

				# If r/c doesn't contain n and the cell is available
				if not hasn and ((horiz and puz[ppos+i][wpos+p] == 0) or (not horiz and puz[wpos+p][ppos+i] == 0)):
					# Increase the count and save the position
					fcnt += 1
					findex = wpos+p

			# If the count is one
			if fcnt == 1:

				# Set the indices for r/c
				if horiz:
					x = ppos+i
					y = findex
				else:
					x = findex
					y = ppos+i

				# And place n at (x,y)
				place_n(puz, x, y, n)