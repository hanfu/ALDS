## find max subarray

## usage: maximize stock gain

## given an array

```python
#recurrsively find max by comparing left half, right half, and midcross
#midcross is bigO(n) complexity
#base condition for left/right halves is len = 1
def max_subarray(arr, start, end):
	if start == end:
		return (arr[start], start, end)
	else:
		mid = (start+end)//2
		lmax = max_subarray(arr, start, mid)
		rmax = max_subarray(arr, mid+1, end)
		cmax = max_cross_subarray(arr, start, mid, end)
		return max((lmax, rmax, cmax), key=lambda x:x[0])

#midcross takes linear time because it must starts from mid
def max_cross_subarray(arr, start, mid, end):
	lmax = max(((sum(arr[i:mid+1]),i) for i in range(start,mid+1)), 
		key = lambda x:x[0])
	rmax = max(((sum(arr[mid+1:i+1]),i) for i in range(mid+1, end+1)), 
		key = lambda x:x[0])
	return (lmax[0]+rmax[0], lmax[1], rmax[1])
	#we need to return more than just max, but also new start and end

```

## algo analysis:

based on recurrsion, write
T(n) = divide.k*T(n.sub) + conquer.n

1. guess T(n), plug back to equation to verify
2. draw recurrsion tree and count n of each level, and # of total levels
3. master method, empirical cookbook method

