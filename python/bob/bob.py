def hey(sentence):
	sentence=sentence.strip()
	x={'Q':'Sure.','yell':'Whoa, chill out!','ntn':'Fine. Be that way!','rand':'Whatever.'}
	if(sentence.isupper()==sentence):
		return(x["yell"])
	elif(sentence.endswith("?")):
		return(x["Q"])
	elif(sentence==0):
		return(x["ntn"])
	else:
		return(x["rand"])
hey("I HATE YOU")