import copy

table = []
endTable = []

with open("input.txt") as textFile:
	for i,line in enumerate(textFile):
		words = line.strip().split(" ")
		table.append([])
		table[i].append(words[4])
		table[i].append(words[0])
		table[i].append(words[2])
endTable = copy.deepcopy(table)


over = False
while not over:
	newTable = []
	print len(endTable)
	for entry in endTable:
		for new in table:
			if entry[len(entry)-1] == new[1]:
				newTable.append([])
				for current in entry:
					newTable[len(newTable)-1].append(current)
				newTable[len(newTable)-1][0] += new[0]
				newTable[len(newTable)-1].append(new[2])
	print len(newTable)
	if len(newTable) == 0:
		over = True
	else:
		endTable = copy.deepcopy(newTable)


print len(endTable)