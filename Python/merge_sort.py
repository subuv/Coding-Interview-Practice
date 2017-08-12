from __future__ import division
import time
import sys

def merge_sort(array):
	if len(array) <= 1:
		return array
	mid = len(array) // 2
	sorted_left_sentinel = merge_sort(array[:mid])
	sorted_right_sentinel = merge_sort(array[mid:])
	return merge(sorted_left_sentinel, sorted_right_sentinel)

def merge(left_sentinel, right_sentinel):
	if not left_sentinel:
		return right_sentinel

	if not right_sentinel:
		return left_sentinel

	if left_sentinel[0] < right_sentinel[0]:
		return [left_sentinel[0]] + merge(left_sentinel[1:], right_sentinel)

	return [right_sentinel[0]] + merge(left_sentinel, right_sentinel[1:])

def main():
	arr = [int(x) for x in raw_input("Enter numbers to be sorted: ").split()]
	start_time = time.time()
	print merge_sort(list(arr))
	end_time = time.time()
	print("Time taken for merge sort is %f " %(end_time - start_time))

main()
