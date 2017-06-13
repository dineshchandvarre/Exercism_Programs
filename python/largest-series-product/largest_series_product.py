def Subtrings(string,n):
	string=	string.replace(" ","")
	li=[]
	for i in range( len( string ) -n+1):
		li.append(string[ i : i+n ])
	return li
def largest_product(string,n):
	productList=[]
	
	s=Subtrings(string,n)
	for element in s:
		a=1
		for digit in element:
			a=a*int(digit)
		k=(element,str(a))
		
		productList.append(k)
	return max(productList)

print(largest_product("123456789",2))

