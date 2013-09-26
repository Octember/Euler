# Surprisingly there are only three numbers that can be written as
#   the sum of fourth powers of their digits:

# 1634 = 1^4 + 6^4 + 3^4 + 4^4
# 8208 = 8^4 + 2^4 + 0^4 + 8^4
# 9474 = 9^4 + 4^4 + 7^4 + 4^4
# As 1 = 14 is not a sum it is not included.

# The sum of these numbers is 1634 + 8208 + 9474 = 19316.

# Find the sum of all the numbers that can be written as the sum of
#   fifth powers of their digits.


import time

def sum_power_digits(n, power):
	answer = 0
	while n != 0:
		answer += (n % 10) ** power
		n /= 10
	return answer

def solve():
	POWER = 5

	solution = 0

	for n in range(2, 1000000):
		if sum_power_digits(n, POWER) == n:
			print n
			solution += n



	print "Solution: {}".format(solution)



if __name__ == "__main__":
	start_time = time.time()

	solve()

	elapsed_time = time.time() - start_time
	print "Elapsed time: {} seconds".format(elapsed_time)
	

# Solution: 443839
# Elapsed time: 2.12700009346 seconds
