fullsize = 0;
ruban = 0;
with open("input.txt") as textFile:
    for line in textFile:
        array = [int(x) for x in line.split("x")]
        size = [array[0]*array[1],array[0]*array[2],array[2]*array[1]]
        fullsize += size[0]*2+size[1]*2+size[2]*2+min(size);
        array.sort();
        ruban += array[0]*2 + array[1]*2 + array[0]*array[1]*array[2];

print "Square meter of paper needed: " + str(fullsize);
print "lengt of ribbon needed: " + str(ruban);