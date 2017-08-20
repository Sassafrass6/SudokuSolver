import numpy as np
from Puzzles import *


# Read 'grid_dim' lines of 'grid_dim' integers.
# 'grid_dim' is currently defined as 9 in 'Puzzles.py'
def read_puzzle ( ):

	puz = np.zeros((grid_dim, grid_dim), dtype=int)
	print('Enter %d lines with %d numbers each.\n* Use enter as line return\n* Use 0s as empty spaces\n* Include digits only\n'%(grid_dim, grid_dim))

	# Save lines into puzzle array
	for i in np.arange(grid_dim):
		s = str(raw_input())
		assert(len(s) == 9)
		puz[i,:] = np.array([int(j) for j in s])

	# Print array in python format
	output = 'puzzle_diff_x = np.array(['
	for i in np.arange(grid_dim):
		output += '['
		for j in np.arange(grid_dim):
			output += str(puz[i][j])
			if j != (grid_dim-1):
				output += ','
		output += ']'
		if i != (grid_dim-1):
			output += ','
	print('\n' + output + '])\n\n')
	
	return puz