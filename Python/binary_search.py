def binary_search(arr, l, r, x):
	if r >= l:
		mid = l + (r-l)//2
		if(arr[mid] == x):
			return mid
		elif arr[mid] > x:
			return binary_search(arr, l, mid - 1, x)
		else:
			return binary_search(arr, mid + 1, r, x)
	else:
		return -1

a = [2, 5, 6, 10, 20, 35]
x = 35
print binary_search(a, 0, len(a)-1, x)
