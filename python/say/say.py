import math
def say(num):
	dictionary={1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen",100: "Hundred and"}
	tens_dictionary= {20: "twenty",30: "thirty",40: "forty",50: "fifty",60: "sixty",70: "seventy",80: "eighty",90: "ninety"} 
	# print(dictionary[num])
	# if(num[])
	n = num
	i = 100 
	while (n>1):
		if(i != 10 ):
			print(dictionary[math.floor(n/i)]+"  "+dictionary[i])
		else:
			print(tens_dictionary[(math.floor(n/i))*10])
		n = n%i
		if(i>1):
			i = i/10
say(1145) 