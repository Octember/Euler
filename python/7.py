# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we 
#   can see that the 6th prime is 13.
#
# What is the 10 001st prime number?

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
	N = 10001

	primes = eratosthenes_sieve(1000000) # How far do we need to go??

	solution = primes[N - 1]

	print "Solution: {}".format(solution)



if __name__ == "__main__":
	start_time = time.time()

	solve()

	elapsed_time = time.time() - start_time
	print "Elapsed time: {} seconds".format(elapsed_time)


# Solution: 104743
# Elapsed time: 0.395999908447 seconds