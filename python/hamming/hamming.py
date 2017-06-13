def distance(a,b):
	nucleotides = {'A': 'U', 'C': 'G', 'G': 'C', 'T': 'A'}
	A=list(a)
	B=list(b)
	print(A)
	print(B)
	count=0
	if(len(a)==len(b)):
		for i in range(len(A)):
			if(A[i]!=B[i]):
				count+=1
		return(count)
	else:
		raise ValueError('length of string doesnt match')