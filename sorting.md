#USAGE: 
sort, find median, binary search
find dup, 

## given array A[]:


## INSERTION SORT
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
def MergeSort(arr):
	if len(arr) == 1:
		return arr[0]
	else:

```