import re
import numpy as np

a = np.zeros((1000,1000), dtype=bool)
b = np.zeros((1000,1000), dtype=int)
total = 0
total2 = 0
with open("input.txt") as textFile:
	for line in textFile:
		SuperPowerRegexParty = re.search(r'^(.*)( )(\d{1,3})(,)(\d{1,3})( through )(\d{1,3})(,)(\d{1,3})$',line.strip())
		command = SuperPowerRegexParty.group(1)
		x1 = int(SuperPowerRegexParty.group(3))
		y1 = int(SuperPowerRegexParty.group(5))
		x2 = int(SuperPowerRegexParty.group(7))
		y2 = int(SuperPowerRegexParty.group(9))
		if (command=="toggle"):
			for x in range(x1,x2+1):
				for y in range(y1,y2+1):
					if a[x,y]:
						a[x,y] = 0
						total -= 1
					else:
						a[x,y] = 1
						total += 1
					b[x,y]+=2
					total2+=2
		elif (command=="turn off"):
			for x in range(x1,x2+1):
				for y in range(y1,y2+1):
					if a[x,y]:
						total -= 1
					a[x,y] = 0
					if b[x,y] != 0:
						b[x,y]-=1
						total2-=1
		elif (command=="turn on"):
			for x in range(x1,x2+1):
				for y in range(y1,y2+1):
					if not a[x,y]:
						total += 1
					a[x,y] = 1
					b[x,y]+=1
					total2+=1
print "Q1: There is ", total, " lights open"
print "Q2: Total lumens for theses lights is ", total2