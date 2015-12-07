code = dict({}) 

with open("input.txt") as textFile:
	for line in textFile:
		values = line.strip().split(' -> ')
		code.update({values[1]:values[0]})

def search(n):
	print n
	if n.isdigit():
		return n
	else:
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

print search('a')
