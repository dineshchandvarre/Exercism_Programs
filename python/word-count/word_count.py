def word_count(phrase):
	 punctuation=['(', ')', '?', ':', ':', ',', '.', '!', '/', '"', "'","_"]
	 for i in punctuation:
	 	phrase=phrase.replace(i," ")
	 a=phrase.split()
	 b=set(a)
	 for word in b:
	   x=a.count(word)
	   if(x>=1):
	     print(word,x,sep =" : ")
# word_count('hey,my_spacebar_is_broken.')
