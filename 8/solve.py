import re

difference = 0
differenceQ2 = 0

with open("input2.txt") as textFile:
    for line in textFile:
        difference += 2
        differenceQ2 += 2
        for match in re.findall(r'(\\x..|\\\\|\\\")', line):
            if match.endswith('\"') or match.endswith('\\'):
                difference += 1
            else:
                difference += 3
        for char in line.strip():
            if char == '\\' or char == '\"':
                differenceQ2 += 1

print "Q1: The number of char difference is ", difference
print "Q2: The number of char difference is ", differenceQ2