import numpy as np
from Puzzles import *
from SolveMethods import *
from AuxilaryMethods import *

# Attempt to complete blocks, rows and coloumns that only have one free cell
# Only blocks are implemented thus far.
def complete_brc ( puz ):

	print('complete_brc')
	madeReplacement = False
	npos = np.empty((2), dtype=bool)
	hasn = np.zeros((grid_dim), dtype=bool)
	#	Complete Blocks
	for i in np.arange(0, grid_dim, block_dim):
		for j in np.arange(0, grid_dim, block_dim):
			ncnt = 0
			nvar = np.zeros((grid_dim), dtype=bool)
			for ik in np.arange(block_dim):
				for jk in np.arange(block_dim):
					x = i + ik
					y = j + jk

					if puz[x][y] == 0:
						ncnt += 1
						npos = np.array([x, y])
					else:
						hasn[puz[x][y]-1] = True

			if ncnt == 1:
				for tn in np.arange(grid_dim):
					if not hasn[tn]:
						print 
						puz[npos[0], npos[1]] = tn+1
						madeReplacement = True
						break

		return madeReplacement


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
				
					print('Outer block Method')
				outer_block_method(puz, True, n)
				outer_block_method(puz, False, n)

				if not (prevPuz == puz).all():
					continue

				if verbose:
					print('Inner block Method')
				inner_block_method(puz, n)

				if not (prevPuz == puz).all():
 					continue

				if verbose:
					print('Row Method')
				line_method(puz, True, n)
				line_method(puz, False, n)

		# If the puzzle didnt change in this iteration break loop and verify puzzle
		# Otherwise update the iteration count and continue
		if (prevPuz == puz).all():
#			if complete_brc(puz):
#				continue
			prevPuz = None
			break
		else:
			iterCount += 1
			continue

	print('\nFinal Puzzle')
	display_puzzle(puz)

	# Update numsCompleted
	find_completed_numbers(puz, numsComplete)

	# Verify that the Sudoku is correct
	if not verify_puzzle(puz):
		print 'Puzzle Inconsistent'
	if numsComplete.all():
		print 'Puzzle Solved!'
		print '--------------\n\n'
