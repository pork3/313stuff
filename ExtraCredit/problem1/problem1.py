''' help with k order : https://users.cs.fiu.edu/~giri/teach/5407/F05/LecX2.pdf
'''

from enum import Enum
import sys


class Color(Enum):
	RED = 1
	BLACK = 2

class RBNode:
	def __init__(self, x, t_dot_nil, subtreesize = None):
		self.key = x
		self.subtreesize = 0
		self.color = Color.RED
		self.left = t_dot_nil
		self.right = t_dot_nil
		self.parent = t_dot_nil

	def __str__(self):
		return repr(self.key)

class RedBlackTree:

	class EmptyTree(Exception):
		def __init__(self, data = None):
			super().__init__(data)

	class NotFound(Exception):
		def __init__(self,data=None):
			super().__init__(data)

	class InvalidSubtree(Exception):
		def __init__(self, data = None):
			super().__init__(data)

	def __init__(self):
		self.root = self.nil = RBNode(None,None)
		self.nil.color = Color.BLACK

	def left_rotate(self, x):
		y = x.right
		x.right = y.left
		if y.left != self.nil:
			y.left.parent = x
		y.parent = x.parent
		if x.parent == self.nil:
			self.root = y
		elif x == x.parent.left:
			x.parent.left = y
		else:
			x.parent.right = y
		y.left = x
		x.parent = y

	def right_rotate(self, x):
		y = x.left
		x.left = y.right
		if y.right != self.nil:
			y.right.parent = x
		y.parent = x.parent
		if x.parent == self.nil:
			self.root = y
		elif x == x.parent.left:
			x.parent.left = y
		else:
			x.parent.right = y
		y.right = x
		x.parent = y

	def insert(self, z):
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
		z.color = Color.RED
		self.insert_fixup(z)

	def insert_fixup(self, z):
		while z.parent.color == Color.RED:
			if z.parent == z.parent.parent.left:
				y = z.parent.parent.right
				if y.color == Color.RED:
					z.parent.color = Color.BLACK
					y.color = Color.BLACK
					z.parent.parent.color = Color.RED
					z = z.parent.parent
				else:
					if z == z.parent.right:
						z = z.parent
						self.left_rotate(z)
					z.parent.color = Color.BLACK
					z.parent.parent.color = Color.RED
					self.right_rotate(z.parent.parent)
			else:
				y = z.parent.parent.left
				if y.color == Color.RED:
					z.parent.color = Color.BLACK
					y.color = Color.BLACK
					z.parent.parent.color = Color.RED
					z = z.parent.parent
				else:
					if z == z.parent.left:
						z = z.parent
						self.right_rotate(z)
					z.parent.color = Color.BLACK
					z.parent.parent.color = Color.RED
					self.left_rotate(z.parent.parent)
		self.root.color = Color.BLACK

	def search_iterative(self, x,k):
		while x !=self.nil and k !=x.key:
			if k < x.key:
				x = x.left
			else:
				x = x.right
		return x

	def search(self, x , k ):
		z = self.search_iterative(x , k)
		if z == self.nil:
			raise RedBlackTree.NotFound("Search item not found")
		return z

	def minimum(self, x):
		if x == self.nil:
			raise RedBlackTree.EmptyTree("empty tree")
		while x.left != self.nil:
			x = x.left
		return x

	def maximum(self , x):
		if x == self.nil:
			raise RedBlackTree.EmptyTree("Empty Tree")
		while x.right != self.nil:
			x = x.right
		return x

	def transplant(self , u , v):
		if u.parent == self.nil:
			self.root = v
		elif u == u.parent.left:
			u.parent.left = v
		else:
			u.parent.right = v
		v.parent = u.parent

	def remove(self , x):
		z = self.search_iterative(self.root , x.key)
		if z == self.nil:
			raise RedBlackTree.NotFound("Unable to find element")
		y = z
		y_col = y.color
		if z.left == self.nil:
			x = z.right
			self.transplant(z , z.right)
		elif z.right == self.nil:
			x = z.left
			self.transplant(z , z.left)
		else:
			y = self.minimum(z.right)
			y_col = y.color
			x = y.right
			if y.parent == z:
				x.parent = y
			else:
				self.transplant(y , y.right)
				y.right = z.right
				y.right.parent = y
			self.transplant(z , y)
			y.left = z.left
			y.left.parent = y
			y.color = z.color
		if y_col == Color.BLACK:
			self.remove_fixup(x)


	def remove_fixup(self , x):
		while x !=self.root and x.color == Color.BLACK:
			if x == x.parent.left:
				w = x.parent.right
				if w.color == Color.RED:
					w.color = Color.BLACK
					x.parent.color = Color.RED
					self.left_rotate(x.parent)
					w = x.parent.right
				if w.left.color == Color.BLACK and w.right.color == Color.BLACK:
					w.color = Color.RED
					x = x.parent
				else:
					if w.right.color == Color.BLACK:
						w.left.color = Color.BLACK
						w.color = Color.RED
						self.right_rotate(w)
						w = x.parent.right
					w.color = x.parent.color
					x.parent.color = Color.BLACK
					w.right.color = Color.BLACK
					self.left_rotate(x.parent)
					x = self.root
			else:
				w = x.parent.left
				if w.color == Color.RED:
					w.color = Color.BLACK
					x.parent.color = Color.RED
					self.right_rotate(x.parent)
					w = x.parent.left
				if w.right.color == Color.BLACK and w.left.color == Color.BLACK:
					w.color = Color.RED
					x = x.parent
				else:
					if w.left.color == Color.BLACK:
						w.right.color = Color.BLACK
						w.color = Color.RED
						self.left_rotate(w)
						w = x.parent.left
					w.color = x.parent.color
					x.parent.color = Color.BLACK
					w.left.color = Color.BLACK
					self.right_rotate(x.parent)
					x = self.root
		x.color = Color.BLACK	

	def preorder_helper(self, x, l):
		if n !=self.nil:
			l.append(n.key)
			self.preorder_helper(n.left , l)
			self.preorder_helper(n.right , l)

	def to_list_preorder(self):
		l = []
		self.preorder_helper(self.root , l)
		return l

	def inorder_helper(self , n , l):
		if n != self.nil:
			self.inorder_helper(n.left , l)
			l.append(n.key)
			self.inorder_helper(n.right , l)

	def to_list_inorder(self):
		l = []
		self.inorder_helper(self.root , l)
		return l

	def sub_size(self, node):
		l = self.sub_size(node.left) if node.left != self.nil else 0
		r = self.sub_size(node.right) if node.right != self.nil else 0
		node.subtreesize = (l + r) + 1
		return node.subtreesize



	def small_lab(self , node , k):
		if k < 1 or k > self.root.subtreesize:
			raise RedBlackTree.InvalidSubtree("Invalid kth element size")
		r = node.left.subtreesize + 1
		if k == r:
			print(node)
		elif k < r:
			self.small_lab(node.left, k)
		else:
			self.small_lab(node.right, k - r) 

def driver():
	rbt = RedBlackTree()
	f = open(sys.argv[1], "r")
	n = int(f.readline().strip())
	for _ in range(n):
		l = f.readline().strip()
		if l == 'get_subtree_sizes':
			rbt.sub_size(rbt.root)
		else:
			v = l.split()
			if v[0] == 'insert':
				k = int(v[1])
				z = RBNode(k , rbt.nil)
				rbt.insert(z)
			elif v[0] == 'order':
				k = int(v[1])
				try:
					rbt.small_lab(rbt.root,k)
				except RedBlackTree.InvalidSubtree as n:
					print('TreeError')
	f.close()

if __name__ == "__main__":
	driver()







