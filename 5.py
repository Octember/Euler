# 2520 is the smallest number that can be divided by each of the numbers
#   from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible
#   by all of the numbers from 1 to 20?

import time

def get_factors(num):
	factors = []
	for i in range(2, int(num ** 0.5 + 1)):
		if num % i == 0:
			factors.append(i)
			factors.extend(get_factors(num / i))
			return factors
	return [num]

def list_to_dict(factors):
	dictionary = {}
	for number in factors:
		if number in dictionary:
			dictionary[number] += 1
		else:
			dictionary[number] = 1
	return dictionary

def maximize_dicts(dict1, dict2):
	dictionary = {}
	for key in dict1:
		dictionary[key] = dict1[key]
	for key in dict2:
		if key in dictionary:
			dictionary[key] = max(dict1[key], dict2[key])
		else:
			dictionary[key] = dict2[key]
	return dictionary

def solve():
	N = 20

	multiples = [i for i in range(1, N + 1)]

	factor_dicts = [list_to_dict(get_factors(i)) for i in multiples]

	solution_dict = factor_dicts[0]
	for dictionary in factor_dicts[1:]:
		solution_dict = maximize_dicts(dictionary, solution_dict)

	solution = 1
	for key in solution_dict:
		solution *= key ** solution_dict[key]

	print "Solution: {}".format(solution)



if __name__ == "__main__":
	start_time = time.time()

	solve()

	elapsed_time = time.time() - start_time
	print "Elapsed time: {} seconds".format(elapsed_time)


# Solution: 232792560
# Elapsed time: 0.00100016593933 seconds