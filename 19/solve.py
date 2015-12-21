from sets import Set

size = 1
query = ""
changes = []


with open("input.txt") as textFile:
    for line in textFile:
    	data = line.strip().split(" => ")
    	if len(data) == 2:
    		changes.append([])
    		changes[len(changes)-1].append(data[0])
    		changes[len(changes)-1].append(data[1])
    	else:
    		query = data[0]

def onLoop(str):
	result = Set([])
	for sss in str:
		for ch in changes:
			tmp = sss.split(ch[0])
			for i in range(1,len(tmp)):
				result.add(ch[0].join(tmp[:i])+ch[1]+ch[0].join(tmp[i:]))
	return result

longeur = 0
done = False
fullData = Set([query])

while not done:
	longeur += 1
	result = Set([])

	for sss in fullData:
		for ch in changes:
			tmp = sss.split(ch[1])
			for i in range(1,len(tmp)):
				result.add(ch[1].join(tmp[:i])+ch[0]+ch[1].join(tmp[i:]))
	fullData = Set([query])
	for i in range(size):
		fullData.add(min(result, key=len))
		result.remove(min(result, key=len))
	if "e" in fullData:	
		done =True

print "There is this number of molecule ", len(onLoop([query]))
print "Minimum number of iteration to get the molecule ", longeur