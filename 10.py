# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

import time

def eratosthenes_sieve(limit):
	primes = [True] * limit
	primes[0] = False
	primes[1] = False

	for index, is_prime in enumerate(primes):
		if is_prime:

			for i in range(index * 2, limit, index):
				primes[i] = False
	return [i for i in range(len(primes)) if primes[i]]

def solve():
	primes = eratosthenes_sieve(2000000)
	solution = sum(primes)

	print "Solution: {}".format(solution)

if __name__ == "__main__":
	start_time = time.time()

	solve()

	elapsed_time = time.time() - start_time
	print "Elapsed time: {} seconds".format(elapsed_time)


# Solution: 142913828922
# Elapsed time: 0.796000003815 seconds