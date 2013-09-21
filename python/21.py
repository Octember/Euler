# Let d(n) be defined as the sum of proper divisors of n 
#   (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a =/= b, then a and b are an
#   amicable pair and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 
#   1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
#   The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.

import time

from functions import get_divisors

def is_amicable(n):
	pair = sum(get_divisors(n))
	return sum(get_divisors(pair)) == n and pair != n

def solve():
	solution = 0
	for i in range(2, 10000):
		if is_amicable(i):
			solution += i
			print i


	print "Solution: {}".format(solution)



if __name__ == "__main__":
	start_time = time.time()

	solve()

	elapsed_time = time.time() - start_time
	print "Elapsed time: {} seconds".format(elapsed_time)

# Solution: 31626
# Elapsed time: 0.266999959946 seconds 