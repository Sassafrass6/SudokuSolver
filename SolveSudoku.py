import numpy as np
from Puzzles import *
from SolveMethods import *
from AuxilaryMethods import *

def solve_puzzle_suite ( ):
	solve_puzzle(puzzle_easy_1)
	solve_puzzle(puzzle_moderate_1)
	solve_puzzle(puzzle_moderate_2)
	solve_puzzle(puzzle_moderate_3)
	solve_puzzle(puzzle_moderate_4)
	solve_puzzle(puzzle_moderate_5)
	solve_puzzle(puzzle_hard_1)
#	solve_puzzle(puzzle_hard_2)
#	solve_puzzle(puzzle_hard_3)
#	solve_puzzle(puzzle_hard_4)

# Attempts to solve Sudoku puzzle
def solve_puzzle ( puz ):
	
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

		# Use the memory matrix to find cells which can be occupied by only one number
		memory_method(puz, memMat)
		
#		numSol = guess_method(puz)

		# If the puzzle didnt change in this iteration
		if (prevPuz == puz).all():
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
		print 'Puzzle Not Solved'
		print '-----------------\n\n'
	if numsComplete.all():
		print 'Puzzle Solved!'
		print '--------------\n\n'