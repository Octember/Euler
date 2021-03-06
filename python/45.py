# Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:

# Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
# Pentagonal	Pn=n(3n-1)/2 	1, 5, 12, 22, 35, ...
# Hexagonal	 	Hn=n(2n-1)	 	1, 6, 15, 28, 45, ...
# It can be verified that T285 = P165 = H143 = 40755.

# Find the next triangle number that is also pentagonal and hexagonal.

# t(t+1)/2 = p(3p-1)/2 = h(2h-1)
# 
# 

import time

def triangle_numbers(N_limit):
	for n in range(1, N_limit + 1):
		yield (n * (n + 1) / 2)

def pentagonal_numbers(N_limit):
	for n in range(1, N_limit + 1):
		yield (n * (3 * n - 1) / 2)

def hexagonal_numbers(N_limit):
	for n in range(1, N_limit + 1):
		 yield (n * (2 * n - 1))


def solve():
	triangles = triangle_numbers(100000)
	pentagons = pentagonal_numbers(100000)
	hexagons = hexagonal_numbers(100000)

	triangle = triangles.next()
	pentagon = pentagons.next()

	next = False


	for hexagon in hexagons:
		while triangle < hexagon:
			triangle = triangles.next()
		while pentagon < hexagon:
			pentagon = pentagons.next()

		if hexagon == triangle and hexagon == pentagon:
			if next:
				solution = hexagon
				break
			if hexagon == 40755:
				next = True

	print "Solution: {}".format(solution)



if __name__ == "__main__":
	start_time = time.time()

	solve()

	elapsed_time = time.time() - start_time
	print "Elapsed time: {} seconds".format(elapsed_time)

# Solution: 1533776805
# Elapsed time: 0.0460000038147 seconds