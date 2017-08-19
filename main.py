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
	# Solves pre-defined puzzles from 'Puzzles.py'
	solve_puzzle_suite()

	# Records numbers from input
#	solve_puzzle(read_puzzle())