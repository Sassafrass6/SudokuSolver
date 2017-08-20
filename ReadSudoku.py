import numpy as np
from Puzzles import *
from AuxilaryMethods import display_puzzle

# Read 'grid_dim' lines of 'grid_dim' integers.
# 'grid_dim' is currently defined as 9 in 'Puzzles.py'
def read_puzzle ( ):

	puz = np.zeros((grid_dim, grid_dim), dtype=int)
	print('Enter %d lines with %d numbers each.\n* Use enter as line return\n* Use 0s as empty spaces\n* Include digits only\n'%(grid_dim, grid_dim))

	i = 0
	# Save lines into puzzle array
	while i < grid_dim:
		
		s = ''
		# Loop to allow corrections to mistakes in a line
		while True:

			# Print lines leading up to this line
			print('Type \'del\' to remove the previous line\n')
			for ik in np.arange(i):
				output = '%d > '%ik
				for jk in np.arange(grid_dim):
					output += '%d'%puz[ik,jk]
				print(output)

			# Get user input
			s = str(raw_input('%d > '%i))
			if s == 'del':
				i -= 1
				continue
			if len(s) != grid_dim:
				print('\nLine must contain %d characters\n'%grid_dim)
				continue
			try:
				puz[i,:] = np.array([int(j) for j in s])
			except:
				print('\nLine contained invalid characters\nTry again\n')
				continue
			break

		i += 1

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