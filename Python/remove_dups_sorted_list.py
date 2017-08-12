class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	def print_list(self):
		temp = self.head
		while temp:
			print temp.data
			temp = temp.next

	def remove_duplicates(self):
		curr = self.head
		while (curr is not None):
			runner = curr.next
			while runner and runner.data == curr.data:
				runner = runner.next
			curr.next = runner
			curr = runner
		return self.head

llist = LinkedList()
llist.push(8)
llist.push(8)
llist.push(6)
llist.push(6)
llist.push(4)
llist.push(3)
llist.push(3)
llist.push(1)
 
print "Given linked list"
llist.print_list()
 
llist.remove_duplicates()
 
print "\nReverse linked list"
llist.print_list()
