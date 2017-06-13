def sieve(x):
	lst=[]
	for num in range(2,x):
		
		for i in range(2,num):
			if((num % i ) != 0 and (num%num)==0):
				lst.append(num)
	print(lst)
sieve(10)

			
