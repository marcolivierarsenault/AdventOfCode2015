import itertools
import sys

number = []
total = 0
eachSize = 0
eachSizeQ2 = 0
minimumSize = 2
minimumQE1 = sys.maxint
minimumQE2 = sys.maxint
foundQ1 = False
foundQ2 = False

with open("input.txt") as textFile:
    for line in textFile:
    	number.append(int(line.strip()))

total = sum(number)
eachSize = total/3
eachSizeQ2 = total/4

while not foundQ1 or not foundQ2:
	for gr in itertools.combinations(number, minimumSize):
		if sum(gr) == eachSize:
			minimumQE1 = min(minimumQE1, reduce(lambda x, y: x*y, gr))
			foundQ1 = True
		if sum(gr) == eachSizeQ2:
			minimumQE2 = min(minimumQE2, reduce(lambda x, y: x*y, gr))
			foundQ2 = True
	minimumSize +=1
	if minimumSize > len(number):
		foundQ1 = True
		foundQ2 = True

print "Q1 The minimal QE for the best package is: ", minimumQE1
print "Q2 The minimal QE for the best package is: ", minimumQE2