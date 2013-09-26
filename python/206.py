# Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
# where each "_" is a single digit.


import time
import string

# last digit is 0, so last digit of root must end in 0
# therefore last 2 digits are 0
template = "1_2_3_4_5_6_7_8_900"

# next last digit is 9. So root must have a 7 or 3 as second last digit.

# root_template ends in "70" or "30"

def check_value(N):
	N /= 100
	for i in range(9, 0, -1):
		if N % 10 != i:
			return False
		N /= 100

	return True

def root_generator(min, max):
	value = int(min)
	yield value
	while value <= max:
		value = (value / 100) * 100
		yield value + 30
		yield value + 70
		value += 100

	yield value

def solve():
	minimum = int(string.replace(template, '_', '0'))
	maximum = int(string.replace(template, '_', '9'))

	min_root = minimum ** 0.5
	max_root = maximum ** 0.5

	total = (max_root - min_root) / 50
	
	for index, root in enumerate(root_generator(int(min_root), int(max_root))):
	 	if check_value(root * root):
	 		solution = root
	 		break

	 	if index % 100000 == 0:
	 		print "Checked {} out of {}".format(index, total)

	print "Solution: {}".format(solution)



if __name__ == "__main__":
	start_time = time.time()

	solve()

	elapsed_time = time.time() - start_time
	print "Elapsed time: {} seconds".format(elapsed_time)


# Solution: 1389019170
# Elapsed time: 18.5889999866 seconds