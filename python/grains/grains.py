def on_square(m):
	li=[]
	
	d={}
	x=0
	if(m<1 or m>64):
		raise ValueError
	else:
		for i in range(1,m+1):
			x=2**(i-1)
		return x

# print(on_square(5))



def total_after(n):
	result=0
	for j in range(n+1):
		result+=on_square(j)
		
	return result

# print(total_after(5))