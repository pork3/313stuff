import sys

class Node:
	def __init__ (self , value=None):
		self.value = value

class Heap:

	class HeapError(Exception):
		def __init__self(self , data = None):
			self.message = data
			super().__init__(data)

	#made changes based on slides/suggestions
	def __init__(self , size = 0, nList = []):
		self.size = 0
		self.nList = []
	
	def to_string(self):
		if self.is_empty():
			raise Heap.HeapError("Empty")
		else: 
			l = []
			for i in range (0, self.size-1):
				l.append(str(self.nList[i].value))
			print(' '.join(l))

	def sift_down(self , i):
		left = (2 * i) + 1
		right = (2 * i )+ 2
		smallest = i

		if left <= self.size and self.nList[left].value < self.nList[smallest].value:
			smallest = left
		if right <= self.size and self.nList[right].value < self.nList[smallest].value:
			smallest = right
		if smallest != i:
			temp = self.nList[i].value
			self.nList[i].value = self.nList[smallest].value
			self.nList[smallest].value = temp
			self.sift_down(smallest)

	def sift_up(self , i):
		parent = (i - 1) //2		#parent is larger than child node
		while i > 0 and self.nList[parent].value > self.nList[i].value:	
			temp = self.nList[i].value
			self.nList[parent].value = self.nList[i].value
			self.nList[i].value = temp
			i = parent
			parent = (i - 1) // 2

	def insert(self , val):
		n = Node(val)
		self.nList.append(n)
		self.size +=1
		self.sift_up( self.size -1)

	def remove(self ):
		val = self.nList[0].value

		#swap first and last
		self.nList[0].value = self.nList[self.size -1].value
		self.size -=1
		self.sift_down(0)

	def look(self):
		if self.is_empty():
			raise Heap.HeapError("HeapError")
		else:
			return self.nList[0].value	

	def size(self):
		return self.size -1

	def is_empty(self):
		return self.size == 0


def driver():
    h = Heap()
    with open(sys.argv[1]) as f:
        n = int(f.readline().strip())
        for _ in range(n):
            in_data = f.readline().strip().split()
            action, value_option = in_data[0], in_data[1:]
            if action == "insert":
                value = int(value_option[0])
                h.insert(value)
            elif action == "remove":
                try :
                	v = h.remove()
                	print(v)
                except Heap.HeapError:
                	print("HeapError") #just printing exception message rather than exit per
            elif action == "print": #project specifications
            	try:
            		h.to_string()
            	except Heap.HeapError("HeapError"):
            		print("Empty")
            elif action == "size":
            	sz = h.size
            	print(sz)
            elif action == "best":
            	try:
            		v = h.look()
            		print(v)
            	except Heap.HeapError("HeapError"):
            		print("HeapError")


# this starter code should work with either python or python3
if __name__ == "__main__":
    driver()






