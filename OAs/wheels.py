def tyre(x):
	if(x%2==0):
		if(x>=4):
			a=x//4
			b=x%4
			print(a)
			return a + tyre(b)
		elif(x==2):
			return 1
		else:
			return 1
	else:
		return 0
d=[6, 3, 2]

f=[]
for i in range(len(d)):
	x=tyre(d[i])
	f.append(x)
print(f)
