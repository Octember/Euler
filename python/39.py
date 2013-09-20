# If p is the perimeter of a right angle triangle with integral length sides,
#   {a,b,c}, there are exactly three solutions for p = 120.

# {20,48,52}, {24,45,51}, {30,40,50}

# For which value of p <= 1000, is the number of solutions maximised?



# a^2 + b^2 = c^2
# a + b + c = p
#

import time

def solve():

	perimeter_solutions = {}

	for p in range(10, 1001):
		solutions = 0
		for a in range(int(p/2)):
			for b in range(int(p/2)):
				c = (a * a + b * b) ** 0.5
				if a + b + c > p:
					break
				if int(c) != c:
					continue
				if a + b + c == p:
					solutions += 1
		print p, solutions
		perimeter_solutions[p] = solutions / 2


	most = 0
	solution = 0
	for p in perimeter_solutions:
		if perimeter_solutions[p] > most:
			most = perimeter_solutions[p]
			solution = p



	print "Solution: {}".format(solution)



if __name__ == "__main__":
	start_time = time.time()

	solve()

	elapsed_time = time.time() - start_time
	print "Elapsed time: {} seconds".format(elapsed_time)


# Solution: 840
# Elapsed time: 32.8539998531 seconds