def bubble_sort(arr):
	count=0
	for i in range(len(arr)-1):
		for j in range(len(arr)-count):
			if (arr[j]>arr[j+1]):
				arr[j],arr[j+1]=arr[j+1],arr[j]
	count+=1
bubble_sort(7,2,3,5,1,4)
