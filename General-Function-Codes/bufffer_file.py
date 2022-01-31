L = ['E', 'F', 'B', 'A', 'D', 'I', 'I', 'C', 'B', 'A', 'D', 'D', 'E', 'D']

#create dictionary to count frequency

d = {}
for _ in L :
	if _ in d :
		d[_] = d[_] + 1 
	else:
		d[_] = 1

print("d: " , d)

sorteddict = dict(sorted(d.items(), key = lambda k:k[-1] , reverse = True))
print("sorteddict: ",sorteddict) 


newsorteddict = dict(sorted(d.items(), key = lambda tip: (-tip[-1],tip[0]) , reverse = False))
print("newsorteddict: " , newsorteddict) 