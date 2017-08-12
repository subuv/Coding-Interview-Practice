# Find maximum sum of a subsequence in an array such that no consecutive elements are part of this subsequence
# Dynamic Programming in Python
# Time Complexity: O(n)

def find_max_sum(a):
	incl = 0
	excl = 0
	for i in arr:
		new_excl = excl if excl > incl else incl
		incl = excl + i
		excl = new_excl
	return excl if excl > incl else incl

arr = [10,2,3,4,5,6,7,8,9]
print find_max_sum(arr)
