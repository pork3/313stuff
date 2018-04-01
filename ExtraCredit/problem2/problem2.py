import RBT

class Map:
	def __init__():
		self.Tree = RedBlackTree()

	def insert(self,key, value):
		#change the node to create a kvp
		iNode = Node(key,value)
		self.Tree.insert(iNode)

	def reassign(self , key, value):
		z = self.Tree.search(key)
		if z == self.Tree.nil:
			raise EXCEPTIOn
		#change value

	def remove(self, key):
		#raise exception
		self.Tree.remove(key)

	def lookup(self, key):
		return node = self.Tree.search(key)

	def fetch(self, key):
		node = self.Tree.search(key)
		return node.value


