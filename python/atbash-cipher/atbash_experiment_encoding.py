import string
def encode(s):
	d={" ":""}
	a=list(string.ascii_lowercase())
	reverse=a[::-1]
	for i in range(len(a)):
		d[a[i]]=reverse[i]
	for x in list(s):
		if x in d:
			list(s).replace(x,d[x],1)
	r=" ".join(list(s),5)
	return r
encode("mindblowing")



