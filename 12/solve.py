import re
total = 0

f = (open("input.txt")).read()
for num in re.findall(r'(\-*\d+)',f.strip()):
    total += int(num)

found = False
while not found:
	if f.isdigit():
		found = True
	for num in re.findall(r'(\{[^{}]+\})',f.strip()):
		if re.search(r':\"red\"',num) is None:
			tt = 0
			for nn in re.findall(r'(\-*\d+)',num.strip()):
				tt += int(nn)
			f = f.replace(num, str(tt))
		else:
			f = f.replace(num,"0")
print "Final number is: ", total
print "Final no red number is: ", f