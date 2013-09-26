# The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.


import time

def solve():
	LIMIT = 1000

	total = 0

	for i in range(1, LIMIT + 1):
		total += i ** i

	solution = str(total)[-10:]

	print "Solution: {}".format(solution)



if __name__ == "__main__":
	start_time = time.time()

	solve()

	elapsed_time = time.time() - start_time
	print "Elapsed time: {} seconds".format(elapsed_time)


# Solution: 9110846700
# Elapsed time: 0.0769999027252 seconds