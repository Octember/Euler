# Each new term in the Fibonacci sequence is generated by adding the
# previous two terms. By starting with 1 and 2, the first 10 terms will be:
#
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
# By considering the terms in the Fibonacci sequence whose values do not
# exceed four million, find the sum of the even-valued terms.
# 
# 

import time


def fibonacci_generator(limit):
	low = 0
	high = 1
	while high < limit:
		high = high + low
		low = high - low
		yield high

def solve():

	limit = 4000000

	sum_evens = sum([number for number in fibonacci_generator(limit) if number % 2 == 0])

	print "Solution: {}".format(sum_evens)



if __name__ == "__main__":
	start_time = time.time()

	solve()

	elapsed_time = time.time() - start_time
	print "Elapsed time: {} seconds".format(elapsed_time)


# Solution: 4613732
# Elapsed time: 0.00100016593933 seconds