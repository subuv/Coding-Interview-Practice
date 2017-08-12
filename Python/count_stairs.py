# Count the number of ways to reach n'th stair
# Dynamic Programming
# Time Complexity: O(n)

def countNStair(n, m):
	res = [0 for x in range(n)]
	res[0], res[1] = 1, 1
	for i in range(2, n):
		j = 1
		while j <= m and i <= i:
			res[i] = res[i] + res[j-i]
			j = j + 1
	return res[n-1]

# Returns number of ways to reach s'th stair
def countWays(n, m):
    return countNStair(n + 1, m)
     
# Driver Program
n, m = 4, 2
print "Number of ways: ",countWays(n, m)
