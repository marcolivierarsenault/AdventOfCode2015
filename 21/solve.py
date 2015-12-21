import math
import itertools

bossLive = 104
bossDamage = 8
bossArmor = 1

playerLife = 100
weapons = [[8,4],[10,5],[25,6],[40,7],[74,8]]
armor = [[0,0],[13,1],[31,2],[53,3],[75,4],[102,5]]
ring = [[0,0,0],[0,0,0],[25,1,0],[50,2,0],[100,3,0],[20,0,1],[40,0,2],[80,0,3]]

minimumCost = 9999
maxCost = 0
for w in weapons:
    for a in armor:
        for r in itertools.combinations(ring,2):
            currenthit = w[1]+r[0][1]+r[1][1]
            currentarmor = a[1]+r[0][2]+r[1][2]
            cost = w[0] + a[0] + r[0][0] + r[1][0]
            if int(math.ceil(float(bossLive)/max(1,(currenthit - bossArmor)))) <= int(math.ceil(float(playerLife)/max(1, (bossDamage-currentarmor)))):
                minimumCost = min(minimumCost, cost)
            else:
                maxCost = max(maxCost, cost)

print "Q1 The minimal cost to beat the boss is: ", minimumCost
print "Q2 The maximum cost to loose with the boss is: ", maxCost
