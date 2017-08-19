import numpy as np
from Puzzles import *
from SolveMethods import *
from AuxilaryMethods import *

# Attempts to solve Sudoku puzzle
def solve ( puz ):
	
	# Current Iteration
	iterCount = 1

	# Numbers (0-8 representing 1-9) completed in the Sudoku
	numsComplete = np.zeros((grid_dim), dtype=bool)

	print('Original Puzzle')
	display_puzzle(puz)

	# Copy board to determine if the state has changed
	prevPuz = np.zeros_like(puz)

	# As long as the puzzle is unchanged across iterations.
	while (prevPuz == False).any():

		# Save current state
		prevPuz = np.copy(puz)
		
		# Matrix to remember which numbers can occupy which spaces
		memMat = [[[] for _ in np.arange(grid_dim)] for _ in np.arange(grid_dim)]

		if verbose:
			print('\nITERATION # %d'%iterCount)

		if verbose:
			nempty = find_completed_numbers(puz, numsComplete)
			print('Num Empty: %d'%nempty)
		
		# For number 1 - grid_dim
		for n in np.arange(1,grid_dim+1,1):
			# Only emplace numbers incomplete in the puzzle
			if not numsComplete[n-1]:
				if verbose:
					print('\nStarting n=%d'%n)

				if verbose:
					print('Inner block Method')
				inner_block_method(puz, n, memMat)

				if verbose:
					print('Row Method')
				line_method(puz, True, n)
				line_method(puz, False, n)

		# If the puzzle didnt change in this iteration
		if (prevPuz == puz).all():

			fchange = False
			# Search the memory matrix for cells with only one possibility
			for i in np.arange(grid_dim):
				for j in np.arange(grid_dim):
					if len(memMat[i][j]) == 1:
						n = memMat[i][j][0]
						rhasn, _ = row_contains_num(puz, i, n)
						chasn, _ = col_contains_num(puz, j, n)
						bhasn = block_contains_num(puz, i//grid_dim, j//grid_dim, n)
						# If this possibility is still valid change the puzzle
						if not (rhasn or chasn or bhasn):
							puz[i][j] = n
							fchange = True

			# If the puzzle did not change break the solve loop
			if not fchange:
				prevPuz = None
				break

		# The puzzle is still being solved
		iterCount += 1
		continue

	print('\nFinal Puzzle')
	display_puzzle(puz)

	# Update numsCompleted
	find_completed_numbers(puz, numsComplete)

	# Verify that the Sudoku is correct
	if not verify_puzzle(puz):
		print 'Puzzle Inconsistent\n\n'
	if numsComplete.all():
		print 'Puzzle Solved!'
		print '--------------\n\n'