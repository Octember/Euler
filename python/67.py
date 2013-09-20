# By starting at the top of the triangle below and moving to adjacent
#   numbers on the row below, the maximum total from top to bottom is 23.

# 3
# 7 4
# 2 4 6
# 8 5 9 3

# That is, 3 + 7 + 4 + 9 = 23.

# Find the maximum total from top to bottom in triangle.txt 


import time

def solve():

	data = [[int(num) for num in line.split()] for line in open('python/67data.txt')]

	for row in range(len(data) - 2, -1, -1):
		for col in range(row + 1):
			data[row][col] += max(data[row + 1][col], data[row + 1][col + 1])
		

	solution = data[0][0]

	print "Solution: {}".format(solution)



if __name__ == "__main__":
	start_time = time.time()

	solve()

	elapsed_time = time.time() - start_time
	print "Elapsed time: {} seconds".format(elapsed_time)

# Solution: 7273
# Elapsed time: 0.00600004196167 seconds