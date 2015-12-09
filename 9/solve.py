import copy

table = []
endTable = []

with open("input.txt") as textFile:
	for line in textFile:
		words = line.strip().split(" ")
		table.append([])
		table[len(table)-1].append(words[4])
		table[len(table)-1].append(words[0])
		table[len(table)-1].append(words[2])
		table.append([])
		table[len(table)-1].append(words[4])
		table[len(table)-1].append(words[2])
		table[len(table)-1].append(words[0])
endTable = copy.deepcopy(table)


over = False
while not over:
	newTable = []
	for entry in endTable:
		for new in table:
			if entry[len(entry)-1] == new[1]:
				if new[2] not in entry:
					newTable.append([])
					for current in entry:
						newTable[len(newTable)-1].append(current)
					newTable[len(newTable)-1][0] = int(newTable[len(newTable)-1][0])+int(new[0])
					newTable[len(newTable)-1].append(new[2])
	if len(newTable) == 0:
		over = True
	else:
		endTable = copy.deepcopy(newTable)

print "The shortest path is ", min(endTable)[0]
print "The longest path is ", max(endTable)[0]
