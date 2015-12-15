import itertools
ingredient = []
numberTotal = 100

def loadRecurisve(id,remaining):
    if remaining == 0:
        return 0
    return max()

with open("input.txt") as textFile:
    for line in textFile:
        words = line.strip().split(" ")
        ingredient.append([])
        ingredient[len(ingredient)-1].append(words[0])
        ingredient[len(ingredient)-1].append(int(words[2][:-1]))
        ingredient[len(ingredient)-1].append(int(words[4][:-1]))
        ingredient[len(ingredient)-1].append(int(words[6][:-1]))
        ingredient[len(ingredient)-1].append(int(words[8][:-1]))
        ingredient[len(ingredient)-1].append(int(words[10]))

new_list = [item for item in itertools.product(range(numberTotal+1), repeat=4) if sum(item) == numberTotal]

maxHealty = 0
maxScore = 0
for recette in new_list:
    points = [0]*5
    for yy,item in enumerate(ingredient):
        points[0] += item[1]*recette[yy]
        points[1] += item[2]*recette[yy]
        points[2] += item[3]*recette[yy]
        points[3] += item[4]*recette[yy]
        points[4] += item[5]*recette[yy]
    if(min(points))>0:
        maxScore = max(maxScore, points[0]*points[1]*points[2]*points[3])
    if points[4] == 500:
        maxHealty = max(maxHealty, points[0]*points[1]*points[2]*points[3])

print "The best recette as une valeur de: ", maxScore
print "The best recette Sante as une valeur de: ", maxHealty