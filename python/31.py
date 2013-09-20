# In England the currency is made up of pound, $, and pence, p, 
#   and there are eight coins in general circulation:

# 1p, 2p, 5p, 10p, 20p, 50p, $1 (100p) and $2 (200p).
# It is possible to make $2 in the following way:

# 1x$1 + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p
# How many different ways can $2 be made using any number of coins?

import time

solutions = {1:1}

def num_ways(amount, currencies):
	if amount < 0:
		return 0
	if amount <= 1:
		return amount
	if amount in solutions:
		return solutions[amount]

	ways = 0
	for currency in currencies:
		if currency <= amount:
			ways += num_ways(amount - currency, currencies)
			ways += num_ways(amount - currency, currencies[1:]) 
	return ways

def solve():

	
	currencies = (200, 100, 50, 20, 10, 5, 2, 1)

	for i in range(2, 10):
		solutions[i] = num_ways(i, currencies)
		print i, solutions[i]

	solution = 0
	print "Solution: {}".format(solution)



if __name__ == "__main__":
	start_time = time.time()

	solve()

	elapsed_time = time.time() - start_time
	print "Elapsed time: {} seconds".format(elapsed_time)


# Solution: 
# Elapsed time: 