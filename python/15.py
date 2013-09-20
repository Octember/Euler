# Starting in the top left corner of a 2x2 grid, and only being able to move
#   to the right and down, there are exactly 6 routes to the bottom right corner.

# How many such routes are there through a 20x20 grid?

# 
# 

import time

def solve():
	GRID_SIZE = 20

	grid = [[0 for _ in range(GRID_SIZE + 1)] for _ in range(GRID_SIZE + 1)]

	

	for i in range(GRID_SIZE):
		grid[-1][i] = 1
		grid[i][-1] = 1

	grid[-1][-1] = "start"


	for row in range(GRID_SIZE - 1, -1, -1):
		for i in range(GRID_SIZE - row - 1, -1, -1):
			grid[row + i][row] = grid[row + 1 + i][row] + grid[row + i][row + 1]
			grid[row][row + i] = grid[row + 1][row + i] + grid[row][row + 1 + i]

	
	solution = grid[0][0]
	print "Solution: {}".format(solution)



if __name__ == "__main__":
	start_time = time.time()

	solve()

	elapsed_time = time.time() - start_time
	print "Elapsed time: {} seconds".format(elapsed_time)


# Solution: 137846528820
# Elapsed time: 0.000999927520752 seconds