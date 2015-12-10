import re
line = "3113322113"
for n in range(50):
    newline = ""
    for match in re.findall(r'((\d)\2*)', line):
        newline += str(len(match[0])) + match[1]
    line = newline
    if n == 40-1:
        print "The string length for 40 rep is: ", len(line)
    elif n == 50-1:
        print "The string length for 50 rep is: ", len(line)