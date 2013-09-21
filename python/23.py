# A perfect number is a number for which the sum of its proper divisors 
# is exactly equal to the number. For example, the sum of the proper divisors
# of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

# A number n is called deficient if the sum of its proper divisors is less
# than n and it is called abundant if this sum exceeds n.

# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, 
# the smallest number that can be written as the sum of two abundant numbers is 24.
#  By mathematical analysis, it can be shown that all integers greater than 28123
#  can be written as the sum of two abundant numbers. However, this upper limit
#  cannot be reduced any further by analysis even though it is known that the greatest
#  number that cannot be expressed as the sum of two abundant numbers is less than
#  this limit.

# Find the sum of all the positive integers which cannot be written as the sum 
# of two abundant numbers.

import time
from functions import get_divisors


def is_abundant(n):
	return sum(get_divisors(n)) > n

def solve():


	abundant_numbers = [n for n in range(1, 28124) if is_abundant(n)]

	abundant_sums = set()
	for i in range(len(abundant_numbers)):
		for j in range(len(abundant_numbers)):
			if i + j <= 28123:
				abundant_sums.add(i + j)



	solution = 0

	for i in range(1, 28123):
		if i not in abundant_sums:
			solution += i

	print "Solution: {}".format(solution)



if __name__ == "__main__":
	start_time = time.time()

	solve()

	elapsed_time = time.time() - start_time
	print "Elapsed time: {} seconds".format(elapsed_time)


# Solution: 
# Elapsed time: 