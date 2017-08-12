# Distance between two strings
# Dynamic Programming in Python
# Time Complexity O(mn)
# Space Complexity O(mn)

def levenshtein_distance(s1, s2, m, n):
	result = [[0 for x in range(n+1)] for x in range(m+1)]

	for i in range(m+1):
		for j in range(n+1):

			if i == 0:
				result[i][j] = j

			elif j == 0:
				result[i][j] = i

			elif s1[i-1] == s2[j-1]:
				result[i][j] = result[i-1][j-1]

			else:
				result[i][j] = 1 + min(result[i][j-1], result[i-1][j], result[i-1][j-1])

	return result[m][n]

str1 = "sunday"
str2 = "saturday"
 
print levenshtein_distance(str1, str2, len(str1), len(str2))
