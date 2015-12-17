totalSize = 150
inputSize = [43,3,4,10,21,44,4,6,47,41,34,17,17,44,36,31,46,9,27,38]

nbOfBootle = 9999
working = 0 
workingDeep = 0 
def goDeeper(id,remaining, ss, deep):
    global working
    global workingDeep
    global nbOfBootle
    if remaining == 0:
        working+=1
        if deep<nbOfBootle:
            nbOfBootle = deep
            workingDeep = 1
        elif deep==nbOfBootle:
            workingDeep+=1
        return
    if id == len(inputSize) or remaining<0:
        return
    #useCurrent
    goDeeper(id+1, remaining-inputSize[id], ss+" "+str(inputSize[id]), deep+1)
    #do not use it
    goDeeper(id+1, remaining, ss, deep)

goDeeper(0,totalSize,'', 0)
print "There is: ", working, " combinaisons"
print "There is: ", workingDeep, " combinaisons using the minimum number of bootle: ", nbOfBootle