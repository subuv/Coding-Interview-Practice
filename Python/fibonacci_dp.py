#Dynamic Programming using python
#Time: O(n)
#Space: O(1)
def fibonacci(n):
	a=0
	b=1
	if n < 0:
		print "Incorrect input. Check!"
	elif n==0:
		return a
	elif n ==1:
		return b
	else:
		for i in range(2,n):
			# b = b + a
			# a = b - a
			c = a + b
			a = b
			b = c
		return b

print fibonacci(10)
