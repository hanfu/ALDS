#this not working, because of scope
'''
def swap(a,b):
	temp = a
	a = b
	b = temp
'''
#this works but tedious
'''
def swap(a,b):
	return b,a
x,y = swap(x,y)
'''
#so for python, just use x,y = y,x

'''
def InsertionSort(arr):
	for i in range(1,len(arr)):
		j = i-1
		while arr[i] < arr[j] and j>0:
			arr[i], arr[j] = arr[j], arr[i]
			j = j-1
			i = i-1
	return arr
'''
#important to have j>0 otherwise it can go negetive
#and the algo still work but mess up the result
#no swap, but remember the key

def InsertionSort(arr):
	for i in range(1,len(arr)):
		j = i
		key = arr[i]
		while key < arr[j-1] and j>0:
			arr[j] = arr[j-1]
			j = j-1
		arr[j] = key

def SelectionSort(arr):
	for i in range(0,len(arr)-1):
		min = i
		for j in range(i+1, len(arr)):
			if arr[j] < arr[min]:
				min = j
		arr[i], arr[min] = arr[min], arr[i]
	return arr

'''
def select_min(arr):
	min = arr[0]
	for i in arr:
		if i < min:
			min = i
	return min
'''