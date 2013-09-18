# If we list all the natural numbers below 10 that are
# multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.

import time


def Run():
	upper_limit = 1000
	divisors = (3, 5)

	def is_multiple(number, divisors):
		for divisor in divisors:
			if number % divisor == 0:
				return True
		return False

	multiples = [number for number in range(upper_limit) if is_multiple(number, divisors)]
	sum_multiples = sum(multiples)

	print "Solution: {}".format(sum_multiples)



if __name__ == "__main__":
	start_time = time.time()

	Run()

	elapsed_time = time.time() - start_time
	print "Elapsed time: {} seconds".format(elapsed_time)