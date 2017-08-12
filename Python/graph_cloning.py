class Node:
	def __init__(self, d):
		self.data = d
		self.neighbors=[]

def clone_rec(root, nodes_completed):
	if root is None:
		return None

	p_new = Node(root.data)
	nodes_completed[root] = p_new

	for p in root.neighbors:
		x = nodes_completed.get(p)

		if x == None:
			p_new.neighbors += [clone_rec(p, nodes_completed)]
		else:
			p_new.neighbors += [x]
	return p_new

def clone(root):
  nodes_completed = {}
  return clone_rec(root, nodes_completed)
