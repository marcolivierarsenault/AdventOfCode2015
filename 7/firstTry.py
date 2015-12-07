import operator
code = dict({}) 
occurence = dict({}) 

with open("input.txt") as textFile:
	for line in textFile:
		values = line.strip().split(' -> ')
		code.update({values[1]:values[0]})
		occurence.update({values[1]:0})


y = 0
def search(n):
	global y
	y+=1
	if (y>(2**288+1000)):
		return "HERE"
	if n.isdigit():
		return n
	else:
		occurence[n] += 1
		original = code[n]
		if "AND" in original:
			digit = original.split(" ")
			output = "( " + search(digit[0]) + " & " + search(digit[2]) + " )"
			return output
		elif "OR" in original:
			digit = original.split(" ")
			output = "( " + search(digit[0]) + " | " + search(digit[2]) + " )"
			return output
		elif "LSHIFT" in original:
			digit = original.split(" ")
			output = "( " + search(digit[0]) + " << " + digit[2] + " )"
			return output
		elif "RSHIFT" in original:
			digit = original.split(" ")
			output = "( " + search(digit[0]) + " >> " + digit[2] + " )"
			return output
		elif "NOT" in original:
			digit = original.split(" ")
			output = "(~"+ search(digit[1]) +" & 0xffff)"
			return output
		else:
			return search(original)

print eval(search('a'))
print sorted(occurence.items(), key=operator.itemgetter(1))