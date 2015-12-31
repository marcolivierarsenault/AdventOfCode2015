import copy

userHP = 50
userMana = 500
boseHp = 58
bossDamage = 9
spells = (
[53,4,0,0,0,0], #cost, damage, heal, armor, mana, turn
[73,2,2,0,0,0],
[113,0,0,7,0,6],
[173,3,0,0,0,6],
[229,0,0,0,101,5],
)


minimumMana = 99990

def loopin(turn, userhp, userMana, bossHp, totalMana, spellInProgress, sss, q):
	global minimumMana
	global spells
	armor = 0
	if q and turn % 2 == 1:
		userhp-=1
	if totalMana >= minimumMana or turn > 20 or userMana <= 0 or userhp <= 0:
		i =0
	else:
		for sp in spellInProgress:
			if sp[5]>0:
				if sp[1] > 0:
					bossHp -= sp[1]
				elif sp[3] > 0:
					armor += sp[3]
				elif sp[4] > 0:
					userMana += sp[4]
				sp[5] -= 1

		if bossHp <= 0:
			minimumMana = min(minimumMana,totalMana)
		if turn % 2 == 1:
			for sp in spells:
				if sp[5] == 0:
					newSpell = copy.deepcopy(spellInProgress)
					loopin(turn+1, userhp+sp[2], userMana-sp[0], bossHp-sp[1], totalMana+sp[0], newSpell, sss + str(sp[0])+";",q )
				else:
					newSpell = copy.deepcopy(spellInProgress)
					already = False
					for n in newSpell:
						if sp[0] == n[0] and n[5]>0:
							already = True
					if not already:
						newSpell.append(copy.deepcopy(sp))
						loopin(turn+1, userhp, userMana-sp[0], bossHp, totalMana+sp[0], newSpell, sss + str(sp[0]) + ";",q)
		else:
			loopin(turn+1, userhp - max(1,bossDamage-armor), userMana, bossHp, totalMana, spellInProgress, sss,q)

spellInProgress = []
loopin(1,userHP,userMana,boseHp,0,spellInProgress, "", False)
print "Q1", minimumMana
minimumMana = 99999
loopin(1,userHP,userMana,boseHp,0,spellInProgress, "", True)
print "Q2", minimumMana