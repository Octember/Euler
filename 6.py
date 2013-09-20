# The sum of the squares of the first ten natural numbers is,
#
# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
#
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural
#   numbers and the square of the sum is 3025 - 385 = 2640.
#
# Find the difference between the sum of the squares of the first one hundred
#   natural numbers and the square of the sum.


import time

def solve():
	N = 100

	sum_squares = sum([i*i for i in range(1, N + 1)])
	square_sum = sum([i for i in range(1, N + 1)]) ** 2

	solution = square_sum - sum_squares

	print "Solution: {}".format(solution)


if __name__ == "__main__":
	start_time = time.time()

	solve()

	elapsed_time = time.time() - start_time
	print "Elapsed time: {} seconds".format(elapsed_time)


# Solution: 25164150
# Elapsed time: 0.00100016593933 seconds