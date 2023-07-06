class singly_linked_list: 
	def __init__(self, value):
		self.type = 'S'
		self.next = None
		self.value = value
		self.length = 0
		self.last_ = None

class doubly_linked_list:
	def __init__(self, value):
		self.type = 'D'
		self.next = None
		self.prev = None
		self.value = value
		self.length = 0 
		### only for the last node 
		self.last_ = None
		


class handle_linked_list:
	def create_single_linked_list(data): # data passed as an array [x,y,z,....]
		if len(data) == 0 : return "data lenght is null , can't create a link list !"
		root = None
		current = None
		index = 0 
		for x in data:
			node=singly_linked_list(x)
			if index == 0 :
				root = node
				index= 1
			if current :current.next = node
			else:current = node
			current = node
			root.length +=1
		print('DONE !')
		root.last_ = current
		return root
	def extract_singly_linked_list(root):
		current_node = root
		while True:
			if current_node.next == None:
				print(current_node.value)
				break
			print(current_node.value)
			current_node = current_node.next
	######
	def create_doubly_linked_list(data):
		if len(data) == 0 : return "data lenght is null , can't create a link list !"
		root = None
		current = None
		prev = None
		index = 0 
		for x in data:
			node=doubly_linked_list(x)
			if index == 0 :
				root = node
				index= 1
			if current:
				node.prev = current
				current.next = node 

			prev = current
			current = node
			root.length+=1
		root.last_ = current
		print('DONE !')
		return root
	def extract_doubly_linked_list(root, mode):# (mode=0| from index 0 to n) (mode=1|from index n to 0 )
		if mode == 0:
			current_node = root
			while True:
				if current_node.next == None:
					print(current_node.value)
					break
				print(current_node.value)
				current_node = current_node.next
		elif mode == 1 :
			current_node = root.last_
			while True:
				if current_node.prev == None:
					print(current_node.value)
					break

				print(current_node.value)
				current_node = current_node.prev
	######
	def insert_into_single_linked_list(root,value, mode):#(0 insert at the beginning)(1 insert at last)
		node = singly_linked_list(value)
		if mode == 0 :
			node.next = root
			node.last_ = root.last_
			return node
		elif mode == 1 :
			root.last_.next = node
			root.last_ = node
			return root
	def pop_first(root):
		root_ = None
		if root.next:
			root_ = root.next
			root_.last_ = root.last_
			root.next = None
		else:
			print("No items left ")
			return 0
		return root_

	def pop_last(root):pass


"""
root = handle_linked_list.create_single_linked_list([1,'amine','ezra',15,15241,'JS SUCKS(probably bc i suck at it :)'])
handle_linked_list.extract_singly_linked_list(root)
print('-----')
root = handle_linked_list.insert_into_single_linked_list(root, "newvalue", 0)
handle_linked_list.extract_singly_linked_list(root)
print('-----')
handle_linked_list.insert_into_single_linked_list(root,"oldest_value", 1)
handle_linked_list.extract_singly_linked_list(root)
print('-----')
root = handle_linked_list.pop_first(root)
handle_linked_list.extract_singly_linked_list(root)
"""
#root = handle_linked_list.create_doubly_linked_list([1,'amine','ezra',15,15241,'JS SUCKS(probably bc i suck at it :)'])
#handle_linked_list.extract_doubly_linked_list(root,1)
#print(root.length-1)