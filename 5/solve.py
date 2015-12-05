import re

i = 0
y = 0
with open("input.txt") as textFile:
    for line in textFile:
        if re.search(r'^((?!ab|cd|pq|xy).)*$',line) and re.search(r'(\w)\1+',line) and re.search(r'(.*[aeiou]){3}.*',line):
        	i+=1
        if re.search(r'^.*([a-zA-Z])(.)\1.*$',line) and re.search(r'.*(\w)(\w).*\1\2.*',line):
        	y+=1
print "P1: There is ", i, "good words"
print "P2: There is ", y	, "good words"