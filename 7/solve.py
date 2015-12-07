import re
input = dict({}) 
originalInput = dict({}) 


with open("input.txt") as textFile:
    for line in textFile:
        values = line.strip().split(' -> ')
        input.update({values[1]:values[0]})
originalInput = input.copy()

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

def resolveDic(code):
    anwser = dict({}) 
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
    return anwser

a1 = resolveDic(input)['a']
originalInput['b'] = str(a1)
a2 = resolveDic(originalInput)['a']

print "Q1: The value of A is: ", a1
print "Q2: The value of A is: ", a2