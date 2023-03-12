#used linked list instead of list because push and pop in list O(n) whereas in linked list it is O(1)
# Node class 
class Node:
	def __init__(self,data):
		self.data = data
		self.next = None
	
class Stack:
	
	# constructor initializing head with None
	def __init__(self):
		self.head = None

	def isempty(self):
		return True if self.head == None else False

	
	def push(self,data):
		if self.head == None:
			self.head=Node(data)
		else:
			new_node = Node(data)
			new_node.next = self.head
			self.head = new_node
	
	
	def peek(self):
		if self.isempty():
			return None
		else:
			return self.head.data
	
	
	# pop method will remove the current head and return its value
	def pop(self):
		if self.isempty():
			return None
		else:
			popped_node = self.head
			self.head = self.head.next
			popped_node.next = None
			return popped_node.data
			
stack_obj = Stack()

stack_obj.push(5)
stack_obj.push(2)
stack_obj.push(7)
stack_obj.push(8)

print(stack_obj.peek())
print(stack_obj.pop())

print(stack_obj.peek())
print(stack_obj.pop())

print(stack_obj.peek())
print(stack_obj.pop())