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

def InsertionSort(list):
	for i in range(1,len(list)):
		j = i-1
		while list[i] < list[j]:
			list[i], list[j] = list[j], list[i]
			j = j-1
			i = i-1
	return list
