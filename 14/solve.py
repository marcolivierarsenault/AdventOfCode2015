tableDistance = []
Distance = 2503
maxValue = [0]*Distance

with open("input.txt") as textFile:
    for line in textFile:
        words = line.strip().split(" ")
        speed = int(words[3])
        time = int(words[6])
        rest = int(words[13])
        currentDistance = 0
        tableDistance.append([])
        for i in range(Distance):
            if (i % (time+rest) < time):
                currentDistance+=speed
            if currentDistance > maxValue[i]:
                maxValue[i] = currentDistance
            tableDistance[len(tableDistance)-1].append(currentDistance)

maxLenght = 0
for n in tableDistance:
    if n[len(n)-1] > maxLenght:
        maxLenght = n[len(n)-1]

pts = [0]*len(tableDistance)
for i in range(Distance):
    for j in range(len(tableDistance)):
        if tableDistance[j][i] == maxValue[i]:
            pts[j] += 1

print "The fastest reindeer went: " + str(maxLenght)
print "The reindeer with more points has: " + str(max(pts))
