from __future__ import division
import time
import sys

def selection_sort(array):
	n = len(array)
	for i in range(n-1, 0, -1):
		max_position = 0
		for j in range(1, i+1):
			if array[j]>array[max_position]:
				max_position = j
		tmp = array[i]
		array[i] = array[max_position]
		array[max_position] = tmp

	return array

def main():
	arr = [int(x) for x in raw_input("Enter numbers to be sorted: ").split()]
	start_time = time.time()
	print selection_sort(list(arr))
	end_time = time.time()
	print("Time taken for selection sort is %f " %(end_time - start_time))

main()
