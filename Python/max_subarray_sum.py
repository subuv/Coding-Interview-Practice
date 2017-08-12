# Maximum subarray sum
# Dynamic Programming algorithm
# Time O(n)
#Space

def maxSubArraySum(a, size):
    max_so_far = a[0]
    curr_max = a[0]
     
    for i in range(1,size):
        curr_max = max(a[i], curr_max + a[i])
        max_so_far = max(max_so_far,curr_max)
         
    return max_so_far

a = [-5, -4, -2, -3, 1, 4, -1, -2, 1, 5, -2, -3]
print "Maximum contiguous sum is" , maxSubArraySum(a,len(a))
