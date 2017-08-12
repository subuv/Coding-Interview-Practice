from __future__ import division
import time
import sys

# def partition(array, low, high):
# 	i = (low - 1)
# 	pivot = array[high]

# 	for j in range(low, high):
# 		if array[j] <= pivot:
# 			i = (i+1)
# 			array[i], array[j] = array[j], array[i]

# 	array[i+1], array[high] = array[high], array[i+1]
# 	return (i+1)

def partition(myList, start, end):
    pivot = myList[(start+end)//2]
    left = start+1
    # Start outside the area to be partitioned
    right = end
    done = False
    while not done:
        while left <= right and myList[left] <= pivot:
            left = left + 1
        while myList[right] >= pivot and right >=left:
            right = right -1
        if right < left:
            done= True
        else:
            # swap places
            temp=myList[left]
            myList[left]=myList[right]
            myList[right]=temp
    # swap start with myList[right]
    temp=myList[start]
    myList[start]=myList[right]
    myList[right]=temp
    return right

def quick_sort(array, low, high):
	if low < high:
		pi = partition(array, low, high)

		quick_sort(array, low, (pi-1))
		quick_sort(array, (pi+1), high)
	return array

def main():
	array = [int(x) for x in raw_input("Enter numbers to be sorted: ").split()]
	n = len(array)
	start_time = time.time()
	print quick_sort(list(array), 0, n-1)
	end_time = time.time()
	print("Time taken for quick sort is %f " %(end_time - start_time))

main()
