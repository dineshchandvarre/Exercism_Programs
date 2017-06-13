def abbreviate(s):
	a=list(s.split())
	newstring=""
	for i in range(len(a)):
		newstring+=a[i][0]
	return newstring.upper()

abbreviate("Ruby on Rails nhh  s s ")