#!/usr/bin/python3
import sys

## Check if no arguments given
if len(sys.argv) == 1:
	print("Please give file name with name of author then contents.")
	print("Have no blank lines!!")
	print("File must end with 10 dashes")
	print("Separate authors by 10 dashes like so:")
	print("----------")
	print("\n")
	print("Usage example:\npython3 words.py fileName\n ./words.py filename")
	exit(1)

## Check if too many arguments
if len(sys.argv) > 3:
	print("Too many arguments")
	exit(1)
elif len(sys.argv) < 2:
	print("Too few arguments")
	exit(1)

## Get file name
try:
	if sys.argv[0] == "python" or sys.argv[0] == "python3":
		f = open(sys.argv[2], "r")
		d = open(sys.argv[2], "r")
	else:
		f = open(sys.argv[1], "r")
		d = open(sys.argv[1], "r")
except:
	print("Failed to open file")
	exit(1)

## Function that checks for number of different words
def numWords(a):
	s = a.split()
	num = 0
	used = []
	for x in s:
		## Removing all unnecessary characters
		edit = x.lower().replace(" ", "").replace("(", "").replace(")", "").replace(",", "").replace("'", "").replace("\"", "").replace("[", "").replace("]", "").replace(".", "").replace(";", "").replace("-", "").replace("?", "").replace("!", "").replace("~", "").replace("`", "").replace("\"", "").replace("/", "")
		if edit not in used:
			used.append(edit)
			num += 1
	return(num)

## Function that returns index of greatest value from list
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

## Same as maxIndex, but leaves out a value
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

## Grab authors name and lyrics
authors = []
lyrics = []
lineNum = 0
artistNum = 1
for i in d:
	if i.rstrip() == "":
		continue
	templyrics = ""
	if lineNum == 0:
		authNext = True
	for x in f:
		if x.rstrip() == "":
			continue
		lineNum += 1
		if authNext:
			authors.append(x.rstrip())
			authNext = False
			continue
		if "----------" in x.split():
			authNext = True
			artistNum += 1
			break
		templyrics += x.replace("\n", " ")
	lyrics.append(templyrics)
f.close()
d.close()

## Remove any null values and doctor list
lNew = []
for x in lyrics:
	if x == '':
		continue
	x = x.split()
	x = " ".join(x)
	lNew.append(str(x))

lyrics = lNew

## Grab longest word
longest = []
for i in lyrics:
	tempLong = ""
	for x in i.split():
		x = x.replace(",", "").replace(".", "").replace("!", "").replace("\"", "").replace(";", "")
		if len(x) > len(tempLong):
			tempLong = x
	longest.append(tempLong)

# print("Authors:")
# print(authors)
# print("Lyrics:")
# print(lyrics)

## Who is superior????
uWords = []
for x in lyrics:
	uWords.append(numWords(x))
# print("uWords:")
# print(uWords)

## Get artists and stats
first = authors[maxIndex(uWords)]
firstWords = uWords[maxIndex(uWords)]
second = authors[maxIndexExc(uWords, uWords[maxIndex(uWords)])]
secondWords = uWords[maxIndexExc(uWords, uWords[maxIndex(uWords)])]
uSort = []
for x in uWords:
	uSort.append(x)
uSort.sort(reverse=True)

print("Ranked by number of unique words as follows:")
counter = 1

for x in uSort:
	print("{}.\t{} with {} words".format(counter, authors[uWords.index(x)], x))
	counter += 1

## Make sorted list of longest
longSort = []
for x in longest:
	longSort.append(x)
longSort.sort(key=len, reverse=True)

print("\nRanked by longest used word as follows:")
counter = 1

for x in longSort:
	print("{}.\t{} with {} characters in \"{}\"".format(counter, authors[longest.index(x)], len(x), x))
	counter += 1
