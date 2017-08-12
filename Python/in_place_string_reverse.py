s = raw_input("Enter the string: ")
s_list = []
s_list.extend(s)
n = len(s_list)

for i in range(0, n/2):
	s_list[i], s_list[n-i-1] = s_list[n-i-1], s_list[i]

print ''.join(s_list)
