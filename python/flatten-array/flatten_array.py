def flatten(input):
	flat=[]
	for i in input:
		if(isinstance(i,(tuple,list))):
			flat+=flatten(i)
		elif(i!=None):
			flat.append(i)
	return flat
