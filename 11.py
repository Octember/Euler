# In the 20x20 grid below, four numbers along a diagonal line have been marked in red.


# The product of these numbers is 26 x 63 x 78 x 14 = 1788696.

# What is the greatest product of four adjacent numbers in the same direction
#  (up, down, left, right, or diagonally) in the 20x20 grid?

import time

def solve():

	grid = open('11data.txt', 'r')

	data = [[int(number) for number in line.split()] for line in grid]


	solution = 0
	list_product = lambda x, y: x * y

	GRID_SIZE = 20

	# left/right
	for row in range(GRID_SIZE):
		for col in range(GRID_SIZE - 4):
			solution = max(solution, reduce(list_product, data[row][col:col+4]))

	# up/down
	for col in range(GRID_SIZE):
		for row in range(GRID_SIZE - 4):
			product = reduce(list_product, [data[row + i][col] for i in range(4)])
			solution = max(solution, product)

	# diagonal
	for row in range(GRID_SIZE - 4):
		for col in range(GRID_SIZE - 4):
			product1 = reduce(list_product, [data[row + i][col + i] for i in range(4)])
			product2 = reduce(list_product, [data[row + 4 - i][col + i] for i in range(4)])
			solution = max(solution, product1, product2)


	print "Solution: {}".format(solution)



if __name__ == "__main__":
	start_time = time.time()

	solve()

	elapsed_time = time.time() - start_time
	print "Elapsed time: {} seconds".format(elapsed_time)


# Solution: 70600674
# Elapsed time: 0.00200009346008 seconds