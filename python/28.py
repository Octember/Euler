# Starting with the number 1 and moving to the right in a clockwise
#   direction a 5 by 5 spiral is formed as follows:

# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13

# It can be verified that the sum of the numbers on the diagonals is 101.

# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral 
#  formed in the same way?

import time

def solve():
	SIZE = 1001

	spiral = [[0 for _ in range(SIZE)] for _ in range(SIZE)]

	center = (SIZE/2, SIZE/2)
	position = [center[0], center[1] + 1]

	spiral[center[0]][center[1]] = 1

	n = 2
	for i in range(1, SIZE/2 + 1):
		for down in range(i * 2 - 1):
			spiral[position[0]][position[1]] = n
			n += 1
			position[0] += 1
		for left in range(i * 2):
			spiral[position[0]][position[1]] = n
			n += 1
			position[1] -= 1
		for up in range(i * 2):
			spiral[position[0]][position[1]] = n
			n += 1
			position[0] -= 1
		for right in range(i * 2 + 1):
			spiral[position[0]][position[1]] = n
			n += 1
			position[1] += 1
		
	
	solution = sum([spiral[i][i] for i in range(SIZE)]) + \
				sum([spiral[SIZE - i - 1][i] for i in range(SIZE)]) - 1

	print "Solution: {}".format(solution)



if __name__ == "__main__":
	start_time = time.time()

	solve()

	elapsed_time = time.time() - start_time
	print "Elapsed time: {} seconds".format(elapsed_time)


# Solution: 669171001
# Elapsed time: 0.442000150681 seconds