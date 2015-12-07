import re
code = dict({}) 
anwser = dict({}) 

with open("input.txt") as textFile:
    for line in textFile:
        values = line.strip().split(' -> ')
        code.update({values[1]:values[0]})

def search(n):
    if n.isdigit():
        return n
    else:
        original = n
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


while len(code)>0:
    newDict = code.copy()
    for k, v in code.iteritems():
         if re.search(r'^\d+ (AND|OR|LSHIFT|RSHIFT) \d+$',v) or re.search(r'^\d+$',v) or re.search(r'^NOT \d+$',v):
            val = eval(search(v))
            anwser[k] = val
            newDict.pop(k)
            for kk, vv in newDict.iteritems():
                newDict[kk] = re.sub(r'\b%s\b' % k, str(val), vv)
    code=newDict.copy()

print "The value of A is: ", anwser['a']