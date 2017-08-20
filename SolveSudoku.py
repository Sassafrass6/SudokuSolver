import numpy as np
import time
from Puzzles import *
from SolveMethods import *
from AuxilaryMethods import *


# Solve all puzzles
def solve_puzzle_suite ( ):

	solved = []
	ttime = time.time()
	solved.append(start_solve(puzzle_easy_1))
	solved.append(start_solve(puzzle_moderate_1))
	solved.append(start_solve(puzzle_moderate_2))
	solved.append(start_solve(puzzle_moderate_3))
	solved.append(start_solve(puzzle_moderate_4))
	solved.append(start_solve(puzzle_moderate_5))
	solved.append(start_solve(puzzle_hard_1))
	solved.append(start_solve(puzzle_hard_2))
##	solved.append(start_solve(puzzle_hard_3))
	solved.append(start_solve(puzzle_hard_4))
	solved.append(start_solve(puzzle_hard_5))
	solved.append(start_solve(puzzle_hard_6))
	solved.append(start_solve(puzzle_very_hard_1))
	solved.append(start_solve(puzzle_very_hard_2))
	solved.append(start_solve(puzzle_very_hard_3))
	solved.append(start_solve(puzzle_worlds_hardest_telegraph))

	if stopwatch:
		print('Total Time:  %.3f seconds\n'%(time.time() - ttime))
	
	for i in np.arange(len(solved)):
		if not solved[i]:
			print('Puzzle #%d failed'%(i+1))
			return False
	return True


# Starts the solving process
# Returns True if the puzzle was solved and False otherwise
def start_solve ( puz ):

	print('Original Puzzle')
	display_puzzle(puz)

	verify_puzzle(puz)

	solved = solve_puzzle(puz, 1)

	print('\nFinal Puzzle')
	display_puzzle(puz)

	# Verify that the Sudoku is correct
	if not verify_puzzle(puz):
		print 'Puzzle Not Solved'
		print '-----------------\n'
		return False
	else:
		print 'Puzzle Solved!'
		print '--------------\n'
		return True


# Attempts to solve Sudoku puzzle
# iter - The current iteration of the solve loop
# Returns True if the puzzle was solved and False otherwise
def solve_puzzle ( puz, iterCount ):

	# Numbers (0-8 representing 1-9) completed in the Sudoku
	numsComplete = np.zeros((grid_dim), dtype=bool)

	# Update numsCompleted
	find_completed_numbers(puz, numsComplete)

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
		for n in np.arange(1,grid_dim+1, 1):

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

		# If the puzzle didnt change in this iteration
		if (prevPuz == puz).all():		
			if verbose:
				print('Memory Method')
			# Use the memory matrix to find cells which can be occupied by only one number
			if memory_method(puz, memMat):
				continue
			# Guess solution (Currently unsupported)
			if verbose:
				print('Guessing Method')
			guess_solution(puz, memMat, iterCount)
			prevPuz = None
			break

		# The puzzle is still being solved
		iterCount += 1
		continue

	# Update numsCompleted
	find_completed_numbers(puz, numsComplete)

	# Verify that the Sudoku is correct
	if not verify_puzzle(puz):
		return False
	elif numsComplete.all():
		return True


# Recursively guesses a number and checks for correctness
# mm - Memory matrix
# iterCount - Total iteration number
# Returns True if the puzzle was solved and False otherwise
def guess_solution ( puz, mm, iterCount ):

	cmin = 10
	cpos = None
	# For each cell
	for i in np.arange(grid_dim):
		for j in np.arange(grid_dim):
			c = len(mm[i][j])
			# Save the cell with the fewest possibilities
			if c != 0 and c <= cmin:
				cmin = c
				cpos = [i, j]

	if cmin < 10:
		# Keep a copy of the correct puzzle to revert to if the guess is bad
		cpuz = np.copy(puz)
		# For each possible number allowed in saved cell
		for i in np.arange(cmin):
			puz[:,:] = cpuz[:,:]
			n = mm[cpos[0]][cpos[1]][i]
			if verbose:
				print('Guessing %d at position (%d, %d)'%(n, cpos[0], cpos[1]))

			puz[cpos[0]][cpos[1]] = n

			if solve_puzzle(puz, iterCount):
				return True
