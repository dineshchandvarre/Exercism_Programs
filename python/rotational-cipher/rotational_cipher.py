import string
def rotate(s,num):
	
	for i in s:
		if(i.isalpha()):
			n=ord(i)
			x=n+num
			s=s.replace(i,chr(x),1)
	return s
# rotate('abc-}aba',9)




