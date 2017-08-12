# Coin change problem
# Dynamic programming in Python
# Time complexity: O(mn)
# Count coin change inputs
# Set S - indicates the set of denominations
# m - length of the set
# n - Amount required through denominations

def count_coin_change(S, m, n):
	res = [[0 for x in range(m)] for x in range(n + 1)]

	for i in range(m):
		res[0][i] = 1

	for i in range(1, n + 1):
		for j in range(m):
			x = res[i-S[j]][j] if (i-S[j]) >= 0 else 0
			y = res[i][j-1] if j >= 1 else 0

			res[i][j] = x + y

	return res[n][m-1]

arr = [1, 2, 3, 5, 10]
n = 10
print(count_coin_change(arr, len(arr), n))
