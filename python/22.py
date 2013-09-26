# Using 22data.txt, a 46K text file containing over five-thousand first names, 
#   begin by sorting it into alphabetical order. Then working out the
#   alphabetical value for each name, multiply this value by its alphabetical
#   position in the list to obtain a name score.

# For example, when the list is sorted into alphabetical order, COLIN, 
#  which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
#  So, COLIN would obtain a score of 938 x 53 = 49714.

# What is the total of all the name scores in the file?


import time
from string import uppercase

def get_value(name):
	return sum([uppercase.index(letter) + 1 for letter in name])


def solve():
	text = [line for line in open('22data.txt', 'r')][0] # only one line
	names = text.split(',')
	for i in range(len(names)):
		names[i] = names[i][1:-1]
	names = sorted(names)

	solution = 0
	for index, name in enumerate(names):
		solution += get_value(name) * (index + 1)

	print "Solution: {}".format(solution)



if __name__ == "__main__":
	start_time = time.time()

	solve()

	elapsed_time = time.time() - start_time
	print "Elapsed time: {} seconds".format(elapsed_time)


# Solution: 871198282
# Elapsed time: 0.0239999294281 seconds