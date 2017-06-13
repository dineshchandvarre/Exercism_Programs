def slices(s,n):
	x=len(s)-n+1
	y=[]
	for i in range(x):
		tup=s[i:n]
		n+=1
		y.append(list(tup))
		
	print(y)
slices("01234",2)
