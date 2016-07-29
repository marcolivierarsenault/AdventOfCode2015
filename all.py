import os

for x in range (1,26):
    os.chdir(str(x))
    print "================  " + str(x) + "  ================"
    execfile( "solve.py")
    os.chdir("..")
print "================  COMPLETED  ================"