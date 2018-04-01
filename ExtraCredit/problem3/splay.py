import sys

class Node:
	def __init__(self, k):
		self.key = k
		self.left = None
		self.right = None
		self.parent = None

	def __str__(self):
		return repr(self.key)

class SplayTree:

	class EmptyTree(Exception):
		def __init__(self, data = None):
			super().__init__(data)

	def __init__(self):
		self.root = self.nil = Node(None)
		self.height = 0

	def height(self):
		self.height = self.height_helper(self.root)

	def height_helper(self, node):
		l = self.sub_size(node.left) if node.left != self.nil else 0
		r = self.sub_size(node.right) if node.right != self.nil else 0
		h = (l + r) + 1
		return h

	def insert(self, z):
		#maybe nil?
		z = Node(z)
		y = self.nil
		x = self.root
		while x != self.nil:
			y = x
			if z.key < x.key:
				x = x.left
			else:
				x = x.right
		z.parent = y
		if y == self.nil:
			self.root = z
		elif z.key < y.key:
			y.left = z
		else:
			y.right = z
		z.left = z.right = self.nil
		self.splay(z)

	def root_key(self):
		if self.root == self.nil:
			raise SplayTree.EmptyTree("Action performed on empty tree")
		return self.root

	#check...
	def search(self , k):
		x = self.root
		if x == self.nil:
			raise SplayTree.EmptyTree("Search Done on empty Tree")
		
		while x != self.nil and k != x.key:
			#print("parent " + str(x.parent))
			y = x.parent
			if k < x.key:
				x = x.left
			else:
				x = x.right
		if x == self.nil:
			self.splay(y)
		else:
			self.splay(x)
			return x


	def splay(self, x):
		while x != self.root:
			if x.parent == self.root:
				if x == x.parent.left:
					self.right_rotate(x)
				else:
					self.left_rotate(x)
			else:
				if x == x.parent.left:
					if x.parent == x.parent.parent.left:
						self.right_rotate(x)
						self.right_rotate(x)
					else:
						self.right_rotate(x)
						self.left_rotate(x)
				else:
					if x.parent == x.parent.parent.right:
						self.left_rotate(x)
						self.left_rotate(x)
					else:
						self.left_rotate(x)
						self.right_rotate(x)

	def left_rotate(self, x):
		p = x.parent
		x.parent = p.parent
		if p == self.root:
			self.root = x
		elif p == p.parent.left:
			p.parent.left = x
		else:
			p.parent.right = x
		p.right = x.left
		#self.nil maybe
		if p.right != self.nil:
			p.right.parent = p
		x.left = p
		p.parent = x

	def inorder_helper(self , n , l):
		if n != self.nil:
			self.inorder_helper(n.left , l)
			l.append(n.key)
			self.inorder_helper(n.right , l)

	def to_list_inorder(self):
		l = []
		self.inorder_helper(self.root , l)
		return l

	def right_rotate(self, x):
		p = x.parent
		x.parent = p.parent
		if p == self.root:
			self.root = x
		elif p == p.parent.left:
			p.parent.left = x
		else:
			p.parent.right = x
		p.left = x.right
		#self.nil?
		if p.left != self.nil:
			p.left.parent = p
		x.right = p
		p.parent = x


def driver():
	s = SplayTree()
	"""
	s.insert(3)
	s.insert(4)
	s.insert(88)
	s.insert(15)
	s.insert(99)
	print(s.root)
	s.insert(44)
	print(s.root)
	#r = s.root_key()
	#print(r)
	#r = s.search(4)
	r = s.search(1)
	print(s.root)
	#print(s.root)
	#r = s.root_key()
	#print(r)

	"""
	f = open(sys.argv[1], "r")
	n = int(f.readline().strip())
	for _ in range(n):
		l = f.readline().strip()
		if l == 'root':
			try:
				x = s.root_key()
				print(x.value)
			except SplayTree.EmptyTree as et:
				print('Empty')
		elif l == 'height':
			try:
				#kjfkljcheck
				x = s.height()
				print(x)
			except SplayTree.EmptyTree as et:
				print('Empty')
		elif l == 'inprint':
			lst = s.to_list_inorder()
			if len(lst) == 0:
				print('Empty')
			else:
				strings = [str(x) for x in lst]
				print(' '.join(strings))
		else:
			v = l.split()
			if v[0] == 'insert':
				k = int(v[1])
				rbt.insert(k)
			elif v[0] == 'search':
				k = int(v[1])
				try:
					z = rbt.tree_search(k)
					if z != None:
						print('Found')
				except SplayTree.NotFound as nf:
					print('NotFound')
	f.close()

if __name__ == "__main__":
	driver()

