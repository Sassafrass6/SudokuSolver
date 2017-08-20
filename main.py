import numpy as np
from Puzzles import *
from ReadSudoku import *
from SolveSudoku import *

###################################################
#
# A Sudoku Solver
# Frank Cerasoli
# August 2017
#
# User Defined Variables are Located in Puzzles.py
#
# ASSUMPTIONS:
#  * 2D Grid
#  * (grid_dim % block_dim) == 0
###################################################


# Solves currently solvable Sudoku puzzles
if __name__ == '__main__':

	while(True):
		try:
			a = int(input('Please enter an option:\n1) Solve all puzzles\n2) Enter custom puzzle\n0) Exit\n\n$ '))
			print('\n')
			if a == 1:
				# Solves pre-defined puzzles from 'Puzzles.py'
				if solve_puzzle_suite():
					print('All Puzzles Solved!!')
					print('--------------------')
			elif a == 2:
				# Records numbers from input
				start_solve(read_puzzle())
			elif a == 0:
				break
			else:
				raise
		except:
			print('\nInvalid selection!')

		print('\n')