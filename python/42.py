# The nth term of the sequence of triangle numbers is given by, tn = 1/2n(n+1); so the first ten triangle numbers are:

# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

# By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

# Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?

import time
from string import uppercase

def get_value(word):
	return sum([uppercase.index(letter) + 1 for letter in word])


def triangle_nums(limit):
	return [(n * (n + 1) / 2) for n in range(1, limit)]


def solve():
	triangles = triangle_nums(50)

	solution = 0

	text = [line for line in open('42data.txt', 'r')][0]
	words = text.split(',')
	for i in range(len(words)):
		word = words[i][1:-1]
		if get_value(word) in triangles:
			solution += 1

	print "Solution: {}".format(solution)



if __name__ == "__main__":
	start_time = time.time()

	solve()

	elapsed_time = time.time() - start_time
	print "Elapsed time: {} seconds".format(elapsed_time)


# Solution: 162
# Elapsed time: 0.0090000629425 seconds