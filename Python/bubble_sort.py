from __future__ import division
import time
import sys

def bubble_sort(array):
	n = len(array)
	for i in range(n-1, 0, -1):
		for j in range(i):
			if array[j]>array[j+1]:
				tmp = array[j]
				array[j] = array[j+1]
				array[j+1] = tmp

	return array

def main():
	arr = [int(x) for x in raw_input("Enter numbers to be sorted: ").split()]
	start_time = time.time()
	print bubble_sort(list(arr))
	end_time = time.time()
	print("Time taken for bubble sort is %f " %(end_time - start_time))

main()
