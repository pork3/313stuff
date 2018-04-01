import sys

class Node:
	def __init__(self, value = None):
		self.value = value

class Heap:

	class HeapError(Exception):
		def __init__(self, data = None):
			super().__init__(data)

	def __init__(self , nSize = 0, nList = []):
		self.nSize = 0
		self.nList = [0] 

	def is_empty(self):
		return self.nSize == 0

	def to_string(self):
		if self.is_empty():
			print("Empty")
		else:
			l = []
			for i in range (1, self.nSize + 1):
				l.append(str(self.nList[i].value))
			print(' '.join(l))

	def look(self):
		if self.is_empty():
			raise Heap.HeapError("HeapError")
		else:
			return self.nList[1].value

	def insert(self, val):
		node = Node(val)
		self.nSize += 1
		self.nList.append(node) #add node to end of heap

		i = self.nSize#get last element
		parent = i // 2 # parent node

		while i > 1:
			if self.nList[i].value < self.nList[parent].value:
				self.swap(self.nList[i] , self.nList[parent])
			i = i // 2
			parent = i // 2	#maybe add parennt

	def remove(self):
		if self.is_empty():
			raise Heap.HeapError("HeapError")
		else:
			value = self.nList[1].value
			self.swap(self.nList[1] , self.nList[self.nSize - 1]) #put last element at top
			del self.nList[self.nSize - 1]
			self.nSize -=1
		self.heapify(1) #top node may violate heap property
		return value

#sift down
	def heapify(self , index):
		left = 2 * index
		right = 2 * index + 1
		smallest = index

		if left <= self.nSize - 1 and self.nList[left].value < self.nList[smallest].value:
			smallest = left
		if right <= self.nSize -1 and self.nList[right].value < self.nList[smallest].value:
			smallest = right

		if smallest != index:
			self.swap(self.nList[index], self.nList[smallest])
			self.heapify(smallest// 2)

	def swap(self, node1 , node2):
		temp = node1.value
		node1.value = node2.value
		node2.value = temp

	def size(self):
		return self.nSize
"""
def driver():
	h = Heap()
	with open(sys.argv[1]) as f:
		n= int(f.readline().strip())
		for _ in range(n):
			in_data = f.readline().strip().split()
			action , val = in_data[0] , in_data[1:]
			if action == "insert":
				v = val
				h.insert(v)
			elif action == "remove":
				try:
					v = h.remove()
					print(v)
				except Heap.HeapError as e:
					print("HeapError")
			elif action == "print":
				h.to_string()
			elif action == "size":
				print(h.size())
			elif action == "best":
				try:
					v = h.look()
					print(v)
				except Heap.HeapError as e:
					print("HeapError")

"""
def driver():
	h = Heap()
	h.insert(10)
	h.insert(111)
	h.insert(22222)
	h.insert(0)
	h.insert(-11)
	h.insert(-1111)
	h.insert(19)
	h.insert(-9)
	h.insert(8)
	h.insert(-22222222)
	h.to_string()

if __name__ == "__main__":
	driver()