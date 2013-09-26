# A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

# For example,

# 44 -> 32 -> 13 -> 10 -> 1 -> 1
# 85 -> 89 -> 145 -> 42 -> 20 -> 4 -> 16 -> 37 -> 58 -> 89

# Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

# How many starting numbers below ten million will arrive at 89?


import time


chains = {}

def sum_squares(value):
	summation = 0
	while value != 0:
		digit = value % 10
		summation += digit * digit
		value /= 10
	return summation


def find_chain(N):
	if N == 1 or N == 89:
		return N	
	if N in chains:
		return chains[N]
	next = sum_squares(N)
	chains[N] = next
	final = find_chain(next)
	chains[N] = final
	return final

def solve():

	count = 0
	for i in range(1, 10000000):
		if find_chain(i) == 89:
			count += 1

	solution = count
	print "Solution: {}".format(solution)



if __name__ == "__main__":
	start_time = time.time()

	solve()

	elapsed_time = time.time() - start_time
	print "Elapsed time: {} seconds".format(elapsed_time)


# Solution: 8581146
# Elapsed time: 28.4449999332 seconds