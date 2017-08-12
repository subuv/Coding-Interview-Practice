# Imagine a game (like baseball) where a player can score 1, 2 or 4 runs. Given a score "n", find the total number of ways score "n" can be reached.
# Dynamic Programming
# Time Complexity: O(n)

def count_score_possibilities(n):
    res = [0 for x in range(n)]
    res[0] = 1;
    for i in range(1, n):
       res[i] = res[i] + res[i - 1]
    for i in range(2, n):
       res[i] = res[i] + res[i - 2]
    for i in range(4, n):
       res[i] = res[i] + res[i - 4]
    return res[n-1]
 
n = 20
print("Count for %d is %d\n", n, count_score_possibilities(n));

n = 13
print("Count for %d is %d", n, count_score_possibilities(n));
