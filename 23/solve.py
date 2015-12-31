command = []

with open("input.txt") as textFile:
    for line in textFile:
    	command.append(line.strip().split(" "))

def getReg(ss):
	if ss[0] == 'a':
		return 0
	elif ss[0] == 'b':
		return 1

def newPtr(ss):
	pp = 0
	if ss[0] == '+':
		pp += int(ss[1:])
	elif ss[0] == '-':
		pp -= int(ss[1:])
	return pp

def doJob(register):
	ptr = 0
	while ptr < len(command):
		if command[ptr][0] == "hlf":
			reg = getReg(command[ptr][1])
			register[reg] = register[reg]/2
		elif command[ptr][0] == "tpl":
			reg = getReg(command[ptr][1])
			register[reg] = register[reg]*3
		elif command[ptr][0] == "inc":
			reg = getReg(command[ptr][1])
			register[reg] = register[reg]+1
		elif command[ptr][0] == "jmp":
			ptr += newPtr(command[ptr][1]) - 1
		elif command[ptr][0] == "jie":
			if register[getReg(command[ptr][1])] %2 == 0:
				ptr += newPtr(command[ptr][2]) - 1
		elif command[ptr][0] == "jio":
			if register[getReg(command[ptr][1])] == 1:
				ptr += newPtr(command[ptr][2]) - 1
		ptr += 1
	return register[1]

print "Q1 Value of register B: ", doJob([0,0])
print "Q2 Value of register B: ", doJob([1,0])