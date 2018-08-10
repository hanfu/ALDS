# USAGE: 
sort, find median, binary search
find dup, examine fundamental algo designs

ALGORITHMS | SPACE | TIME
--- | --- | ---
__INSERTION__ | in place | n^2
__MERGE__ | n | n logn
__HEAP__ | in place | n logn
__QUICK__ | in place | n logn (exp)
__COUNTING__ | in place | n+k


## given array A[]:


## INSERTION SORT
space: in place
time: bigO(n^2)

```python
def InsertionSort(list):
	for i in range(1,len(list)):
		j = i
		key = list[i]
		while key < list[j-1] and j>0:
			list[j] = list[j-1]
			j = j-1
		list[j] = key
	# no return
```

```cpp
#include <cstdio>
#include <cmath>
#include <iostream>
using namespace std;

void InsertionSort(int arr[], int n)
{
	int i, j, key;
	for(i = 1; i<n; i++)
	{
		j = i;
		key = arr[i];
		while(key < arr[j-1] && j>0)
		{
			arr[j] = arr[j-1];
			j--;
		}
		arr[j] = key;
	}

}
```

## SELECTION SORT
```python
def SelectionSort(arr):
	for i in range(0,len(arr)-1):
		min = i
		for j in range(i+1, len(arr)):
			if arr[j] < arr[min]:
				min = j
		arr[i], arr[min] = arr[min], arr[i]
	return arr

```

```cpp
#include <cstdlib>
#include <cstdio>
#include <iostream>
using namespace std;

void SelectionSort(int arr[], int n)
{
	int i, j, min;
	for(i=0;i<n-1;i++)
	{
		min = i;
		for(j=i+1;j<n;j++)
		{
			if (arr[j] < arr[min])
			{
				min = j;
			}
		}
		//swap(&arr[min], &arr[i]);
		//arr is a pointer, but arr[0] is int
		//so we need &arr[i]
	int min_num = arr[min];
	arr[min] = arr[i];
	arr[i] = min_num;

	}
}

```

## MERGE SORT
```python
def MergeSort(arr, start=0, end=None):
	if not end:
		end = len(arr)
	if end-start>1:
		mid = (end+start)//2
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
```
```cpp
#include <cstdio>
#include <iostream>
#include <algorithm>
using namespace std;
void merge(int arr[], int start, int mid, int end)
{
	int il, ir;
	il = mid-start;
	ir = end-mid;
	int larr[il+1], rarr[ir+1];
	//copy(arr+start,arr+mid, larr)
	//copy(arr+mid, arr+end, rarr)
	for(il=0;il<mid-start;il++)
	{
		larr[il] = arr[start+il];
	}
	larr[il] = 100;
	//for infinity
	//not il+1, because il from last loop is already max+1
	for(ir=0;ir<end-mid;ir++)
	{
		rarr[ir] = arr[mid+ir];
	}
	rarr[ir] = 100;
	il = 0;
	ir = 0;
	int j;

	for(j=0;j<end-start;j++)
	{
		if(larr[il] < rarr[ir])
		{
			arr[j] = larr[il];
			il++;
		} else
		{
			arr[j] = rarr[ir];
			ir++;
		}
	}
}
void MergeSort(int arr[], int start, int end)
{
	if(end-start > 1)
	{
		int mid = (start+end)/2;
		MergeSort(arr, start, mid);
		MergeSort(arr, mid, end);
		merge(arr, start, mid, end);
	}
}

```

## find how far an array is from sorted (count inversions, Q2.4 on CLRS p41)

```python
```

## HEAP SORT

```python
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
```
## QUICKSORT
```python
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
```

## Optimization of Comparison Sort

## TREE SORT

## COUNTING SORT
## RADIX SORT
##BUCKET SORT

## ORDER STATISTIC
FIND i-th NUMBER