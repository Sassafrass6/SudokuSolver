import numpy as np
from Puzzles import *
from SolveSudoku import solve

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
	solve(puzzle_easy_1)
	solve(puzzle_moderate_1)
	solve(puzzle_moderate_2)
	solve(puzzle_moderate_3)
#	solve(puzzle_moderate_4)
#	solve(puzzle_hard_1)
#	solve(puzzle_hard_2)