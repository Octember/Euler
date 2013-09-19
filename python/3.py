# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

import time

def get_factors(num):
	factors = []
	for i in range(2, int(num ** 0.5 + 1)):
		if num % i == 0:
			factors.append(i)
			factors.extend(get_factors(num / i))
			return factors
	return [num]

def solve():

	N = 600851475143 

	factors = get_factors(N)
	solution = sorted(factors)[-1]

	print "Solution: {}".format(solution)



if __name__ == "__main__":
	start_time = time.time()

	solve()

	elapsed_time = time.time() - start_time
	print "Elapsed time: {} seconds".format(elapsed_time)


# Solution: 6857
# Elapsed time: 0.0130000114441 seconds