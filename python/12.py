# The sequence of triangle numbers is generated by adding the natural numbers.
# So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
# The first ten terms would be:

# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

# Let us list the factors of the first seven triangle numbers:

#  1: 1
#  3: 1,3
#  6: 1,2,3,6
# 10: 1,2,5,10
# 15: 1,3,5,15
# 21: 1,3,7,21
# 28: 1,2,4,7,14,28
# We can see that 28 is the first triangle number to have over five divisors.

# What is the value of the first triangle number to have over five hundred divisors?

import time

def traingle_numbers(limit):
	num = 1
	for i in range(2, limit + 1):
		yield num
		num += i


def eratosthenes_sieve(limit):
	primes = [True] * limit
	primes[0] = False
	primes[1] = False

	for index, is_prime in enumerate(primes):
		if is_prime:

			for i in range(index * 2, limit, index):
				primes[i] = False
	return [i for i in range(len(primes)) if primes[i]]


def prime_factors(n, primes):
	factors = {1:1}
	for prime in primes:
		if prime > n:
			break
		
		elif n % prime == 0:
			factors[prime] = 1
			n /= prime
			while n % prime == 0:
				n /= prime
				factors[prime] += 1

	return factors

def solve():
	primes = eratosthenes_sieve(100)

	for traingle_num in traingle_numbers(10):
		factors = prime_factors(traingle_num)
		



	print "Solution: {}".format(solution)



if __name__ == "__main__":
	start_time = time.time()

	solve()

	elapsed_time = time.time() - start_time
	print "Elapsed time: {} seconds".format(elapsed_time)


# Solution: 
# Elapsed time: 