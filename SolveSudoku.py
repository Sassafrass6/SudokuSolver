import numpy as np
from Puzzles import *
from SolveMethods import *
from AuxilaryMethods import *

def solve_puzzle_suite ( ):
	solved = []
	solved.append(solve_puzzle(puzzle_easy_1))
	solved.append(solve_puzzle(puzzle_moderate_1))
	solved.append(solve_puzzle(puzzle_moderate_2))
	solved.append(solve_puzzle(puzzle_moderate_3))
	solved.append(solve_puzzle(puzzle_moderate_4))
	solved.append(solve_puzzle(puzzle_moderate_5))
	solved.append(solve_puzzle(puzzle_hard_1))
#	solved.append(solve_puzzle(puzzle_hard_2))
#	solved.append(solve_puzzle(puzzle_hard_3))
#	solved.append(solve_puzzle(puzzle_hard_4))
#	solved.append(solve_puzzle(puzzle_hard_5))
	
	for s in solved:
		if not s:
			return False
	return True

def guess_solution ( puz, mm ):
	cmin = 10
	cpos = None
	for i in np.arange(grid_dim):
		for j in np.arange(grid_dim):
			c = len(mm[i][j])
			if c <= cmin:
				cmax = c
				cpos = [i, j]

	if cmin == 2:
		print 'guessing:', mm[cpos[0]][cpos[1]][int(np.round(np.random.random_sample()))]

# Attempts to solve Sudoku puzzle
def solve_puzzle ( puz ):
	
	# Current Iteration
	iterCount = 1

	# Numbers (0-8 representing 1-9) completed in the Sudoku
	numsComplete = np.zeros((grid_dim), dtype=bool)

	print('Original Puzzle')
	display_puzzle(puz)
	
	verify_puzzle(puz)

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

		# For number 1 - grid_dim
		for n in np.arange(1,grid_dim+1,1):
			# Only emplace numbers incomplete in the puzzle
			if not numsComplete[n-1]:
				if verbose:
					print('\nStarting n=%d'%n)

				if verbose:
					print('Row Method')
				line_method(puz, True, n)
				line_method(puz, False, n)

				if verbose:
					print('Inner block Method')
				inner_block_method(puz, n, memMat)

		# Use the memory matrix to find cells which can be occupied by only one number
		# Currently not functional
#		memory_method(puz, memMat)
		
		# Try recursive solution here
		
		# If the puzzle didnt change in this iteration
		if (prevPuz == puz).all():		
			if verbose:
				print('Memory Method')
			if memory_method(puz, memMat):
				continue
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
		return False
	elif numsComplete.all():
		print 'Puzzle Solved!'
		print '--------------\n\n'
		return True