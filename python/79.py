# A common security method used for online banking is to ask the user for three random characters from a passcode. For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.

# The text file, keylog.txt, contains fifty successful login attempts.

# Given that the three characters are always asked for in order, analyse the file so as to determine the shortest possible secret passcode of unknown length.

import time

def solve():
	orders = {}

	attempts = [line.strip() for line in open('79data.txt', 'r')]
	for attempt in attempts:
		for i in range(2):
			if attempt[i] not in orders:
				orders[attempt[i]] = set([attempt[i + 1]])
			else:
				
				orders[attempt[i]].add(attempt[i + 1])

	# find all numbers in passcode
	all_digits = reduce(lambda x,y: x.union(y), [orders[key] for key in orders])
	for key in orders:
		all_digits.add(key)

	# find the first one
	for key in all_digits:
		pass

	print orders
	# first = 7
	# next = [1X, 9X, (3), 2X, 6X]

	# 7 - 3
	# next = [(1), 8X, 6X]

	# 7 - 3 - 1
	# next = [8X, 2X, (6)]

	# 7 - 3 - 1 - 6
	# next = [9X, 8X, (2)]

	# 7 - 3 - 1 - 6 - 2
	# next = [9X, (8)]

	# 7316289
	# solved by hand using dict :)




	solution = 0
	print "Solution: {}".format(solution)



if __name__ == "__main__":
	start_time = time.time()

	solve()

	elapsed_time = time.time() - start_time
	print "Elapsed time: {} seconds".format(elapsed_time)


# Solution: 
# Elapsed time: 