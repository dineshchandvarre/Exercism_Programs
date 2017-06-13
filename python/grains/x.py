
def check(foo):
	# print filter(lambda x: x % 3 == 0, foo)

	print map(lambda x: x % 3 == 0, foo)


	print reduce(lambda x: x % 3 == 0, foo)


check([2, 18, 9, 22, 17, 24, 8, 12, 27])









