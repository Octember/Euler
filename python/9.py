# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


import time

def solve():

	#   a^2 + b^2 = c^2
	#	a + b + c = 1000
	#
	#	c = sqrt(a^2 + b^2)
	#
	#	a + b + sqrt(a^2 + b^2) = 1000
	#	a + b = 1000 - sqrt(a^2 + b^2)
	#	b = (1000(a - 500))/(a - 1000)
	#	

	for a in range(1, 1000):
		b = (1000*(a - 500))/(a - 1000)
		c = (a * a + b * b) ** 0.5
		if b == int(b) and c == int(c):
			solution = int(a * b * c)
			break
	

	print "Solution: {}".format(solution)



if __name__ == "__main__":
	start_time = time.time()

	solve()

	elapsed_time = time.time() - start_time
	print "Elapsed time: {} seconds".format(elapsed_time)

# Solution: 31875000
# Elapsed time: 0.000999927520752 seconds
