# Euler discovered the remarkable quadratic formula:

# n^2 + n + 41

# It turns out that the formula will produce 40 primes for
#   the consecutive values n = 0 to 39. However, 
#   when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41,
#   and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.

# The incredible formula  n^2 - 79n + 1601 was discovered,
#   which produces 80 primes for the consecutive values n = 0 to 79.
#   The product of the coefficients, -79 and 1601, is -126479.

# Considering quadratics of the form:

# n^2 + an + b, where |a| < 1000 and |b| < 1000

# where |n| is the modulus/absolute value of n
# e.g. |11| = 11 and |-4| = 4
# Find the product of the coefficients, a and b, for the quadratic expression
#   that produces the maximum number of primes for consecutive values of n,
#   starting with n = 0.

from functions import eratosthenes_sieve
import time

def test_equation(a, b, primes):
	# n^2 + a*n + b 
	n = 0
	while True: # so we can error out if we don't have enough primes
		value = (n * n + a * n + b)
		if value not in primes:
			return n
		n += 1



def solve():
	primes = eratosthenes_sieve(100000)
	final_a, final_b, longest = 0, 0, 0
	for i in range(len(primes) - 1):
		
		b = primes[i]
		if b > 1000:
			break
		# n^2 + an + 2
		# @ n = 0 => 2
		# @ n = 1 => 1 + a + 2 => 3 so a must equal 0
		# 
		for j in range(len(primes)):
			next_prime = primes[j]
			if next_prime > 1000:
				break
			a = next_prime - b - 1
		# there is only one possible a for each possible b. 
		# the one it takes to reach the next prime.
		# we now have the equation and can see how far it takes us. Easy!
			length = test_equation(a, b, primes)

			if length > longest:
				longest = length
				final_a, final_b = a, b
				print "n^2 + {}n + {} gives {} primes".format(a, b, length)
			

	solution = final_a * final_b





	print "Solution: {}".format(solution)



if __name__ == "__main__":
	start_time = time.time()

	solve()

	elapsed_time = time.time() - start_time
	print "Elapsed time: {} seconds".format(elapsed_time)


# Solution: -59231
# Elapsed time: 6.67300009727 seconds