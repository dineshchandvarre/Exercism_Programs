import math

def numeral(num):
	roman=[]
	a=[int(d) for d in num]
	print(a)
	for i in range(len(a)-1,-1,-1):
		
		if(i==0 and (a[i]==1 or 2 or 3)):
			thdictionary={'1':'M','2':'MM','3':'MMM'}
			roman+=thdictionary[str(a[i])]
			
			hudictionary={"1":"C","2":"CC","3":"CCC","4":"CD","5":"D","6":"VI","7":"VII","8":"VIII","9":"IX"}


		elif(i==3 and a[i]== 1,2,3,4,5,6,7,8,9):
			
			ondictionary={"1":"I","2":"II","3":"III","4":"IV","5":"V","6":"VI","7":"VII","8":"VIII","9":"IX"}
			roman+=ondictionary[str(a[i])]
		else:
			roman+=[str(a[i])]
			
	print(roman)
numeral("1239")