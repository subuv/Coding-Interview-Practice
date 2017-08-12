from __future__ import division
import time
import sys

# INSERTION SORT ALGORITHM:
# INSERTION SORT(A):
# for j=2 to A.length:
# 	key = A[j]
# 	i = j - 1
# 	while i > 0 and A[i] > key:
# 		A[i + 1] = A[i]
# 		i = i - 1
# 	A[i + 1] = key

def insertion_sort(array):
	n = len(array)
	for j in range(1, n):
		key = array[j]
		i = j - 1
		while ((i > 0) and (array[i] > key)):
			array[i + 1] = array[i]
			i = i - 1
		array[i + 1] = key

	return array

def main():
	arr = [int(x) for x in raw_input("Enter numbers to be sorted: ").split()]
	start_time = time.time()
	print insertion_sort(list(arr))
	end_time = time.time()
	print("Time taken for insertion sort is %f " %(end_time - start_time))

main()
