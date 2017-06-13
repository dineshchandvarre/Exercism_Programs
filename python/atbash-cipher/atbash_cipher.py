import string
# def new():
# 	a=string.ascii_lowercase
# 	alphabet=list(a)
# 	reverse=alphabet[::-1]
# 	dictionary={}
# 	for i in range(len(a)):
# 		dictionary[alphabet[i]]=reverse[i]
# 	return dictionary
# 	# print(len(dictionary))
def encode(s):
	a=string.ascii_lowercase
	alphabet=list(a)
	reverse=alphabet[::-1]
	dictionary={" ":" "}
	for i in range(len(a)):

		dictionary[alphabet[i]]=reverse[i]
	print(dictionary)
	for n in s:
		if(n.isalpha()):
			s=s.replace(n,dictionary[n])
			# s.join()
	print(s)
		

encode("abc d")
#     pass


# def decode():
#     pass
