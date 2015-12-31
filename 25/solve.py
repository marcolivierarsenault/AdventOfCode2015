
def getPosi(x, y):
	bix = x + y - 1
	return sum(range(1, bix)) + y

value = getPosi(3010,3019)
#value = getPosi(6,6)
currentCode = 20151125
for n in range(2,value+1):
	currentCode = currentCode * 252533 % 33554393

print currentCode