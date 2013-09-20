# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 2^1000?


import time

def solve():

	solution = sum([int(n) for n in str(2**1000)])

	print "Solution: {}".format(solution)


if __name__ == "__main__":
	start_time = time.time()

	solve()

	elapsed_time = time.time() - start_time
	print "Elapsed time: {} seconds".format(elapsed_time)


# Solution: 1366
# Elapsed time: 0.00100016593933 seconds