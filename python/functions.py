def eratosthenes_sieve(limit):
	primes = [True] * limit
	primes[0] = False
	primes[1] = False

	for index, is_prime in enumerate(primes):
		if is_prime:

			for i in range(index * 2, limit, index):
				primes[i] = False
	return [i for i in range(len(primes)) if primes[i]]


def fibonacci_generator(limit):
	low = 0
	high = 1
	while high < limit:
		yield high
		high = high + low
		low = high - low
