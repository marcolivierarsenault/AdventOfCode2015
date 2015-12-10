import re

line = "3113322113"

for n in range(50):
    print n
    newline = ""
    for match in re.findall(r'((\d)\2*)', line):
        newline += str(len(match[0])) + match[1]
    line = newline

print len(line)