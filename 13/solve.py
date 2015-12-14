import copy

table = []
endTable = []

with open("input.txt") as textFile:
	for line in textFile:
		words = line.strip().split(" ")
		table.append([])
		if(words[2]=="gain"):
			table[len(table)-1].append(int(words[3]))
		else:			
			table[len(table)-1].append(int(words[3])*-1)
		table[len(table)-1].append(words[0])
		table[len(table)-1].append(words[10][:-1])
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

for i,n in enumerate(endTable):
	val = 0
	for new in table:
		if n[len(n)-1] == new[1] and n[1] == new[2]:
			endTable[i][0] += new[0]
			endTable[i].append(endTable[i][1])
#print endTable

worstTable = []
for i,n in enumerate(endTable):
	worst = 999
	for ii,elem in enumerate(n[1:]):
		for new in table:
			if n[ii] == new[2] and n[ii+1] == new[1]:
				endTable[i][0] += new[0]
				tt = int(new[0])
				for lookBack in table:
					if n[ii] == lookBack[1] and n[ii+1] == lookBack[2]:
						tt += int(lookBack[0])
						if (worst > tt):
							worst = tt
	worstTable.append(endTable[i][0] - worst)

print "The best karma is ", max(endTable)[0]
print "The karma with me is ", max(worstTable)
