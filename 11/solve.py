import re

#passC = 'aahgfkcdehh'
passC = 'vzbxkghb'
def loopIn(i):
    global passC
    s = list(passC)
    s[len(s)-1-i] = 'a'
    s[len(s)-1-i-1] = chr(ord(passC[len(s)-1-i-1])+1)
    passC = "".join(s)
    if s[len(s)-1-i-1] == '{':
        loopIn(i+1)

def find():
    found = False
    global passC
    while not found:
        if re.search(r'(\w)\1+.*(\w)\2+',passC) and re.search(r'^((?!i|o|l).)*$',passC) and re.search(r'(abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz)',passC) and re.search(r'(\w)\1+.*\1\1',passC) == None:
            found = True
        else:
            passC = passC[:-1] + chr(ord(passC[-1])+1)
            if passC[-1] == '{':
                loopIn(0)

find()
print "The sequence is: ", passC

passC = passC[:-1] + chr(ord(passC[-1])+1)
if passC[-1] == '{':
    loopIn(0)
find()
print "The next one is sequence is: ", passC