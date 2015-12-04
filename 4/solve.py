import hashlib
f = "ckczppom"
i = 0
found = False
while (not found):
    m = hashlib.md5()
    m.update(f + str(i))
    if(m.hexdigest().startswith("00000")):
        print "5x0 = ", i
    if(m.hexdigest().startswith("000000")):
        found = True
        print "6x0 = ", i
    i+=1