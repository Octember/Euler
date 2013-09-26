# A googol (10100) is a massive number: one followed by one-hundred zeros; 100100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

# Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?
# import time

# Brute force solution:

import time

def sum_digits(value):
	ret = 0
	while value != 0:
		ret += value % 10
		value /= 10
	return ret

def solve():
	solution = 0
	for a in range(1, 101):
		for b in range(1, 101):
			sum = sum_digits(a ** b)
			if sum > solution:
				solution = sum




	print "Solution: {}".format(solution)



if __name__ == "__main__":
	start_time = time.time()

	solve()

	elapsed_time = time.time() - start_time
	print "Elapsed time: {} seconds".format(elapsed_time)


# Solution: 972
# Elapsed time: 0.677999973297 seconds