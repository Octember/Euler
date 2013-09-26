# The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

# Find the sum of all numbers, less than one million, which are palindromic 
#   in base 10 and base 2.

# (Please note that the palindromic number, in either base, may not include 
#   leading zeros.)



import time


def is_palindrome(value):
	s = str(value)
	length = len(s)
	for i in range(length / 2):
		if s[i] != s[length - i - 1]:
			return False
	return True

def to_binary(value):
	binary = ""
	while value > 0:
		if value % 2 == 0:
			binary = "0" + binary
		else:
			binary = "1" + binary
		value /= 2
	return binary

def solve():
	solution = 0
	for i in range(1000000):
		if is_palindrome(i) and is_palindrome(to_binary(i)):
			solution += i
			print i, to_binary(i)

	print "Solution: {}".format(solution)



if __name__ == "__main__":
	start_time = time.time()

	solve()

	elapsed_time = time.time() - start_time
	print "Elapsed time: {} seconds".format(elapsed_time)


# Solution: 872187
# Elapsed time: 0.963999986649 seconds