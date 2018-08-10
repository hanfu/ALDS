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

import unittest
import random


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

def MergeSort(arr, start=0, end=-1):
	if end==-1:
		end = len(arr)
	if start < end:
		mid = (start+end)/2
		MergeSort(arr, start=start, end=mid)
		MergeSort(arr, start=mid+1, end=len(arr))

def MergeSort_extraspace(arr):
	if 1 < len(arr):
		mid = len(arr)//2#floor divide
		#print(mid)
		arr[:mid] = MergeSort(arr[:mid])
		arr[mid:] = MergeSort(arr[mid:])
		#has to assign becuase right hand arr[] reproduce new arr
		#so newarr = arr[] and left hand arr[] refer to original arr
		#so text book change index of arr[start,end] to modify arr onsite
		merge(arr, mid)
	return arr

def MergeSort(arr, start=0, end=None):
	if not end:
		end = len(arr)
	if end-start>1:
		mid = (end+start)//2
		print(start,mid,end)
		MergeSort(arr, start, mid)
		MergeSort(arr, mid, end)
		merge(arr,start, mid, end)

def merge(arr, start, mid, end):
	larr = arr[start:mid] + [float('inf')]
	rarr = arr[mid:end] + [float('inf')]
	il = 0
	ir = 0
	for j in range(end-start):
		if larr[il] > rarr[ir]:
			arr[start+j] = rarr[ir]
			ir += 1
		else:
			arr[start+j] = larr[il]
			il += 1

def count_inversion(arr):
	pass

def reorder(arr, size, i):
	if not size:
		size = len(arr)
	l = 2*(i+1) - 1
	r = 2*(i+1)
	maxnode = None
	if l<size and arr[l] > arr[i]:
		if r<size and arr[r] > arr[i]:
			maxnode = max(l,r,key=lambda k:arr[k])
		maxnode = l
	if maxnode:
		arr[maxnode], arr[i] = arr[i], arr[maxnode]
		reorder(arr, size=size, i=maxnode)

def heapify(arr):
	minleaf = len(arr)//2
	#consider 0-based python index vs. 1-based heap
	for i in range(minleaf-1,-1,-1):
		reorder(arr, size=len(arr), i=i)
def HeapSort(arr):
	heapify(arr)
	for i in range(len(arr)-1, 0, -1):
		arr[0], arr[i] = arr[i], arr[0]
		reorder(arr, size=i, i=0)

def pivot(arr, start, end):
	pvalue = arr[end]
	pivot = start
	i = start
	while i < end:
		if arr[i] <= pvalue:
			arr[pivot], arr[i] = arr[i], arr[pivot]
			pivot+=1
			i+=1
		else:
			i+=1
	arr[end], arr[pivot] = arr[pivot], arr[end]
	return pivot

def QuickSort(arr, start=None, end=None):
	if (start==None) and (end==None):
		start = 0
		end = len(arr)-1
	#pay attention not use if not start/end
	#cuz 0 == False in python, None is safe though
	if start<end:
		p = pivot(arr, start, end)
		QuickSort(arr, start, p-1)
		QuickSort(arr, p+1, end)

def pivot_random(arr, start, end):
	p = random.choice(range(start, end+1))
	arr[p], arr[end] = arr[end], arr[p]
	#instead of re-write, simply swap random p with last element
	return pivot(arr, start, end)

def QuickSort(arr, start=None, end=None):
	if (start==None) and (end==None):
		start = 0
		end = len(arr)-1
	if start<end:
		p = pivot_random(arr, start, end)
		QuickSort(arr, start, p-1)
		QuickSort(arr, p+1, end)

def CountingSort(arr, max):
	countarr = [0]*(max+1)
	sortedarr = arr[*]
	for i in arr:
		countarr[i] += 1
	for i in range(1,max+1):
		countarr[i] = countarr[i] + countarr[i-1]
	#for stability of array
	for i in range(max, -1, -1):
		sortedarr[countarr[arr[i]]]=arr[i]
		countarr[arr[i]] -= 1
	return sortedarr

def OrderStat(arr, start, order, end):
	if start == end:
		return arr[start]#if the only number is left
	pivot = pivot_random(arr, start, end)
	if pivot == order:
		return arr[pivot]
	elif pivot<order:
		OrderStat(arr, pivot+1, start+order-1-pivot, end)
	else:
		OrderStat(arr, start, order, pivot-1)


