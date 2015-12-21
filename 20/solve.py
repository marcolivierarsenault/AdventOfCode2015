
#target = 160
target = 34000000 # divide by 10

currentElf = 1
doneQ1 = False
doneQ2 = False

elf1 = 0
elf2 = 0

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

while not doneQ1 or not doneQ2:
	vv = factors(currentElf)
	value = sum(vv)
	if value*10 >= target and not doneQ1:
		doneQ1 = True
		elf1 = currentElf
	partSum = 0	
	for val in vv:
		if val*50 > currentElf:
			partSum+=val
	if partSum*11 >= target and not doneQ2:
		doneQ2 = True
		elf2 = currentElf
	currentElf += 1

print "Q1 First house with 34000000 gift: ", elf1
print "Q2 First house with 34000000 gift: ", elf2
