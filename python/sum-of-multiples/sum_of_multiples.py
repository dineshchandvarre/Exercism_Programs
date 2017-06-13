def sum_of_multiples(x,[a,b]):
	a=sum([i for i in range(x) if i % a == 0 or i % b == 0])
	print(a)
sum_of_multiples(51,[5,25])