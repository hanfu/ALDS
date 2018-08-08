def BinarySearch_recurr(arr, key, start=0, end=None):
	if not end:
		end = len(arr)-1
		#minus one because end is the last indice of int
		#it naturally solves a lot trouble from end=len
	if start>end:
		return "no"
	mid = (start+end)//2
	if key == arr[mid]:
		return mid
	elif key > arr[mid]:
		return BinarySearch_recurr(arr, key, start=mid+1, end = end)
		#return results from recurrsive stacks
	else:
		return BinarySearch_recurr(arr, key, start=start, end=mid-1)

def BinarySearch_iter(arr, key, start=0, end=None):
	if end == None:
		end = len(arr) - 1
	while start<end:
		mid = (start+end)//2
		if arr[mid]==key:
			return mid
		elif key>arr[mid]:
			start = mid+1
		else:
			end = mid-1
	return "no"