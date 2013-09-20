# The following iterative sequence is defined for the set of positive integers:

# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
# It can be seen that this sequence (starting at 13 and finishing at 1) 
#   contains 10 terms. Although it has not been proved yet (Collatz Problem),
#   it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.

import time

solutions = {1:1}

def get_next_collatz(n):
	return n / 2 if n % 2 == 0 else 3 * n + 1

def get_chain_length(n):
	if n in solutions:
		return solutions[n]
	next = get_next_collatz(n)
	length = get_chain_length(next) + 1
	solutions[n] = length
	return length

def solve():
	limit = 1000000
	solution = 0
	longest = 0
	for i in range(1, limit):
		length = get_chain_length(i)
		if length > longest:
			longest = length
			solution = i


	print "Solution: {}".format(solution)


if __name__ == "__main__":
	start_time = time.time()

	solve()

	elapsed_time = time.time() - start_time
	print "Elapsed time: {} seconds".format(elapsed_time)

# Solution: 837799
# Elapsed time: 1.69299983978 seconds