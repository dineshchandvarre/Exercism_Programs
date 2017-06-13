def hashvalue(string,tablesize):
	x=0
	for i in range(len(string)):
		x+=ord(string[i])
	print(x%tablesize)
hashvalue("dinesh",9)

# def put(string,value):
# 	dict={'string':'value'}
	
