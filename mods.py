## Just tests for the functions within words.py, not a necessary file

def numWords(a):
	s = a.split()
	print(s)
	num = 0
	used = []
	for x in s:
		if x not in used:
			used.append(x)
			num += 1
	return(num)

"""string = "This is a test of a test"
print(numWords(string))"""

def maxIndex(l):
	maxNum = -1
	maxInd = -1
	count = 0
	for x in l:
		if x > maxNum:
			maxNum = x
			maxInd = count
		count += 1
	return(maxInd)
list = [2, 23, 222, 11, 21]
print(maxIndex(list))

def maxIndexExc(l, a):
	maxNum = -1
	maxInd = -1
	count = 0
	for x in l:
		if x == a:
			count += 1
			continue
		if x > maxNum:
			maxNum = x
			maxInd = count
		count += 1
	return(maxInd)
print(list[maxIndexExc(list, list[maxIndex(list)])])
