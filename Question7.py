counter = 1 #This accommodates for '2', the first prime number.
test = 3
while counter < 10001:
	for i in range(2, test + 1):
		if test == i:
			counter += 1
		elif test % i == 0:
			break
		else:
			continue
	if counter < 10001:
		test += 1
	else:
		break
print test
print counter, "!!!"