#usage: 
sort, find median, binary search
find dup, 

#algos

given array A[]
##insertion sort
```python
def InsertionSort(list):
	for i in range(1,len(list)):
		j = i-1
		while list[i] < list[j]:
			list[i], list[j] = list[j], list[i]
			j = j-1
			i = i-1
	return list


```
```cpp
```