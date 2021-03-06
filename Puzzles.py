import numpy as np

# Print placement info
verbose = False

# Time solve methods
stopwatch = True

grid_dim = 9
block_dim = 3

assert grid_dim%block_dim == 0
assert np.sqrt(grid_dim).is_integer()

puzzle_easy_1 = np.array([[7,9,0,0,0,0,3,0,0],[0,0,0,0,0,6,9,0,0],[8,0,0,0,3,0,0,7,6],[0,0,0,0,0,5,0,0,2],[0,0,5,4,1,8,7,0,0],[4,0,0,7,0,0,0,0,0],[6,1,0,0,9,0,0,0,8],[0,0,0,3,0,0,0,0,0],[0,0,9,0,0,0,0,5,4]])

puzzle_moderate_1 = np.array([[0,3,0,0,1,0,8,0,6],[8,0,0,2,0,9,0,7,0],[0,0,0,3,0,0,0,0,0],[0,5,4,0,0,0,7,6,0],[6,0,0,0,3,0,0,0,5],[0,7,8,0,0,0,3,4,0],[0,0,0,0,0,2,0,0,0],[0,6,0,8,0,1,0,0,9],[5,0,7,0,9,0,0,2,0]])

puzzle_moderate_2 = np.array([[8,9,2,0,0,3,0,1,4],[0,0,0,0,0,0,0,0,0],[0,0,0,0,6,8,0,7,0],[4,5,0,0,8,0,0,0,1],[0,0,8,0,0,0,2,0,0],[1,0,3,7,0,0,5,0,0],[0,7,1,0,0,6,0,5,0],[5,0,9,2,0,0,0,8,0],[6,0,0,0,0,7,0,0,9]])

puzzle_moderate_3 = np.array([[3,0,0,6,1,0,0,0,8],[0,0,2,0,3,0,7,6,0],[0,0,0,7,5,0,2,9,0],[0,9,0,8,0,0,0,1,0],[0,4,0,1,7,3,0,5,0],[0,5,0,0,0,9,0,2,0],[0,3,7,0,4,1,0,0,0],[0,2,5,0,8,0,9,0,0],[4,0,0,0,9,7,0,0,2]])

puzzle_moderate_4 = np.array([[0,0,2,0,0,0,0,0,0],[0,0,3,0,1,0,0,0,6],[0,4,0,0,2,0,0,3,0],[1,0,0,0,0,3,0,0,9],[0,0,5,0,0,0,4,0,0],[2,0,0,6,0,0,0,0,8],[0,9,0,0,7,0,0,4,0],[7,0,0,0,8,0,5,0,0],[0,0,0,0,0,0,3,0,0]])

puzzle_moderate_5 = np.array([[0,0,0,0,0,9,7,0,0],[0,4,0,0,0,6,0,5,0],[0,0,0,1,0,5,0,3,4],[4,0,9,0,0,0,8,0,1],[0,0,1,0,0,0,3,0,0],[3,0,7,0,0,0,2,0,5],[5,1,0,2,0,4,0,0,0],[0,3,0,6,0,0,0,7,0],[0,0,2,9,0,0,0,0,0]])

puzzle_hard_1 = np.array([[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,3,0,8,5],[0,0,1,0,2,0,0,0,0],[0,0,0,5,0,7,0,0,0],[0,0,4,0,0,0,1,0,0],[0,9,0,0,0,0,0,0,0],[5,0,0,0,0,0,0,7,3],[0,0,2,0,1,0,0,0,0],[0,0,0,0,4,0,0,0,9]])

puzzle_hard_2 = np.array([[0,0,0,0,3,7,6,0,0],[0,0,0,6,0,0,0,9,0],[0,0,8,0,0,0,0,0,4],[0,9,0,0,0,0,0,0,1],[6,0,0,0,0,0,0,0,9],[3,0,0,0,0,0,0,4,0],[7,0,0,0,0,0,8,0,0],[0,1,0,0,0,9,0,0,0],[0,0,2,5,4,0,0,0,0]])

# Unsolved (Possibly Inconsistent)
puzzle_hard_3 = np.array([[0,0,0,8,4,0,0,0,9],[0,0,1,0,0,0,0,0,5],[8,0,0,0,2,1,4,6,0],[7,0,8,5,0,0,0,9,0],[0,0,0,0,0,0,0,0,0],[0,5,0,0,0,0,3,0,1],[0,2,4,9,1,0,0,0,7],[9,0,0,0,0,0,5,0,0],[3,0,0,0,8,4,0,0,0]])

puzzle_hard_4 = np.array([[4,7,2,0,0,0,9,0,0],[0,0,0,0,7,0,0,0,0],[1,0,0,6,0,0,7,0,0],[0,0,9,5,0,0,4,0,0],[2,0,7,0,0,0,8,0,1],[0,0,5,0,0,4,6,0,0],[0,0,3,0,0,5,0,0,4],[0,0,0,0,8,0,0,0,0],[0,0,4,0,0,0,1,6,9]])

puzzle_hard_5 = np.array([[1,0,0,8,7,5,6,0,0],[0,0,0,0,0,1,9,5,8],[0,0,0,0,0,0,0,1,0],[0,2,0,7,0,0,0,0,6],[0,0,0,2,4,6,0,0,0],[4,0,0,0,0,3,0,7,0],[0,9,0,0,0,0,0,0,0],[3,6,7,5,0,0,0,0,0],[0,0,1,6,8,7,0,0,4]])

puzzle_hard_6 = np.array([[0,0,0,2,0,0,0,6,3],[3,0,0,0,0,5,4,0,1],[0,0,1,0,0,3,9,8,0],[0,0,0,0,0,0,0,9,0],[0,0,0,5,3,8,0,0,0],[0,3,0,0,0,0,0,0,0],[0,2,6,3,0,0,5,0,0],[5,0,3,7,0,0,0,0,8],[4,7,0,0,0,1,0,0,0]])

puzzle_very_hard_1 = np.array([[0,0,8,0,0,5,7,0,2],[3,0,0,4,0,0,0,1,0],[1,6,0,0,0,0,9,0,0],[0,0,2,6,0,0,0,0,4],[0,3,0,0,0,0,0,7,0],[4,0,0,0,0,7,2,0,0],[0,0,3,0,0,0,0,2,9],[0,1,0,0,0,9,0,0,7],[2,0,9,3,0,0,5,0,0]])

puzzle_very_hard_2 = np.array([[8,6,0,0,2,0,0,0,0],[0,0,0,7,0,0,0,5,9],[0,0,0,0,0,0,0,0,0],[0,0,0,0,6,0,8,0,0],[0,4,0,0,0,0,0,0,0],[0,0,5,3,0,0,0,0,7],[0,0,0,0,0,0,0,0,0],[0,2,0,0,0,0,6,0,0],[0,0,7,5,0,9,0,0,0]])

puzzle_very_hard_3 = np.array([[0,0,0,0,0,0,0,7,8],[0,1,2,3,0,0,0,0,9],[0,4,5,6,0,0,0,0,0],[0,7,8,9,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,1,2,3,0],[0,0,0,0,0,4,5,6,0],[3,0,0,0,0,7,8,9,0],[2,6,0,0,0,0,0,0,0]])

puzzle_worlds_hardest_telegraph = np.array([[8,0,0,0,0,0,0,0,0],[0,0,3,6,0,0,0,0,0],[0,7,0,0,9,0,2,0,0],[0,5,0,0,0,7,0,0,0],[0,0,0,0,4,5,7,0,0],[0,0,0,1,0,0,0,3,0],[0,0,1,0,0,0,0,6,8],[0,0,8,5,0,0,0,1,0],[0,9,0,0,0,0,4,0,0]])
