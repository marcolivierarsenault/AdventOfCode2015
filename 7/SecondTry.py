import re
code = dict({}) 
codeM = dict({}) 
i = 0
with open("input.txt") as textFile:
    for line in textFile:
        values = line.strip().split(' -> ')
        code.update({values[1]:values[0]})
        codeM.update({values[1]:values[0]})

for k, v in code.iteritems():
    for kk,vv in codeM.iteritems():
        print i
        i+=1
        codeM[kk] = re.sub(r'\b%s\b' % k, ' ( ' + codeM[k] + ' ) ', vv)

#print "---------------------------------"
#print codeM
print codeM['a']
#print eval(codeM['a'])