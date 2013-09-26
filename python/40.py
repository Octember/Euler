# An irrational decimal fraction is created by concatenating the positive integers:

# 0.123456789101112131415161718192021...

# It can be seen that the 12th digit of the fractional part is 1.

# If dn represents the nth digit of the fractional part, find the value of the
#   following expression.

# d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000

import time

def champernowne_constant(limit):
	for i in range(1, limit):
		n = str(i)
		for letter in n:
			yield int(letter)



def solve():
	digits = [1, 10, 100, 1000, 10000, 100000, 1000000] #arbitrary enough to hardcode
	solution = 1
	for index, n in enumerate(champernowne_constant(1000000)):
		if (index + 1) in digits:
			solution *= n
			print "{} digit : {}".format(index + 1, n)

		if index > 1000001:
			break


	print "Solution: {}".format(solution)



if __name__ == "__main__":
	start_time = time.time()

	solve()

	elapsed_time = time.time() - start_time
	print "Elapsed time: {} seconds".format(elapsed_time)


# Solution: 210
# Elapsed time: 1.19099998474 seconds