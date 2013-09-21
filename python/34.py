# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

# Find the sum of all numbers which are equal to the sum of the factorial
#   of their digits.

# Note: as 1! = 1 and 2! = 2 are not sums they are not included

import time


digit_factorials = [1]

def sum_factorial_digits(n):
	return sum([digit_factorials[int(i)] for i in str(n)])

def solve():
	factorial = 1
	for i in range(1, 10):
		factorial *= i
		digit_factorials.append(factorial)

	# maximum is when 999999 cannot exceed the sum of factorials.
	# 9! = 362880
	# turns out 99999999 - 8 digits - is the limit
	# for i in range(1, 8):
	# 	n = int("9"*i)
	# 	print n, sum_factorial_digits(n)
	# 	if sum_factorial_digits(n) < n:
	# 		print "too high"

	solution = 0

	for n in range(3, 99999999):
		if n == sum_factorial_digits(n):
			print n
			solution += n

	print "Solution: {}".format(solution)



if __name__ == "__main__":
	start_time = time.time()

	solve()

	elapsed_time = time.time() - start_time
	print "Elapsed time: {} seconds".format(elapsed_time)


# Solution: 
# Elapsed time: 