import re

qualities = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0, 'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1}
operation = {'children': 0, 'cats': 1, 'samoyeds': 0, 'pomeranians': -1, 'akitas': 0, 'vizslas': 0, 'goldfish': -1, 'trees': 1, 'cars': 0, 'perfumes': 0}

def checkop(name, value):
    if operation[name] == -1: #less then
        return qualities[name] > value
    elif operation[name] == 0: # Equals
        return qualities[name] == value
    elif operation[name] == 1: #more then
        return qualities[name] < value

with open("input.txt") as textFile:
    for line in textFile:
        SuperPowerRegexParty = re.search(r'Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)',line.strip())
        if int(qualities[SuperPowerRegexParty.group(2)]) == int(SuperPowerRegexParty.group(3)) and int(qualities[SuperPowerRegexParty.group(4)]) == int(SuperPowerRegexParty.group(5)) and int(qualities[SuperPowerRegexParty.group(6)]) == int(SuperPowerRegexParty.group(7)):
            print "Q1 The good sue is: ",  SuperPowerRegexParty.group(1)
        if checkop(SuperPowerRegexParty.group(2),int(SuperPowerRegexParty.group(3))) and checkop(SuperPowerRegexParty.group(4),int(SuperPowerRegexParty.group(5))) and checkop(SuperPowerRegexParty.group(6),int(SuperPowerRegexParty.group(7))):
            print "Q2 The good sue is: ",  SuperPowerRegexParty.group(1)
