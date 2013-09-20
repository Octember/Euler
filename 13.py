# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
# in 13data.txt

import time

def solve():

	summation = sum([int(line) for line in open('13data.txt')])

	solution = str(summation)[:10]

	print "Solution: {}".format(solution)



if __name__ == "__main__":
	start_time = time.time()

	solve()

	elapsed_time = time.time() - start_time
	print "Elapsed time: {} seconds".format(elapsed_time)


# Solution: 5537376230
# Elapsed time: 0.00100016593933 seconds
