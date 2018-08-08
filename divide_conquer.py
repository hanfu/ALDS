def max_subarray(arr, start, end):
	if start == end:
		return (arr[start], start, end)
	else:
		mid = (start+end)//2
		lmax = max_subarray(arr, start, mid)
		rmax = max_subarray(arr, mid+1, end)
		cmax = max_cross_subarray(arr, start, mid, end)
		return max((lmax, rmax, cmax), key=lambda x:x[0])

def max_cross_subarray(arr, start, mid, end):
	lmax = max(((sum(arr[i:mid+1]),i) for i in range(start,mid+1)), 
		key = lambda x:x[0])
	rmax = max(((sum(arr[mid+1:i+1]),i) for i in range(mid+1, end+1)), 
		key = lambda x:x[0])
	return (lmax[0]+rmax[0], lmax[1], rmax[1])
	#we need to return more than just max, but also new start and end
