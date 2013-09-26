# A palindromic number reads the same both ways. The largest palindrome 
#   made from the product of two 2-digit numbers is 9009 = 91 x 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

import time

# I've been dreading writing this method for a while, but I
# can't think of a better solution than this.
def is_palindrome(value):
	s = str(value)
	length = len(s)
	for i in range(length / 2):
		if s[i] != s[length - i - 1]:
			return False
	return True

def solve():

	greatest = 0
	for i in range(1000, 100, -1):
		for j in range(100, 1000):
			val = j * i
			if is_palindrome(val):
				if val > greatest:
					greatest = val
					print val

	solution = greatest
	print "Solution: {}".format(solution)



if __name__ == "__main__":
	start_time = time.time()

	solve()

	elapsed_time = time.time() - start_time
	print "Elapsed time: {} seconds".format(elapsed_time)


# Solution: 906609
# Elapsed time: 0.801999807358 seconds