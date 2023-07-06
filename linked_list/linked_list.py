class singly_linked_list: 
	def __init__(self, value):
		self.type = 'S'
		self.next = None
		self.value = value

class doubly_linked_list:
	def __init__(self, value):
		self.type = 'D'
		self.next = None
		self.prev = None
		self.value = value
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
		print('DONE !')
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
			

#root = handle_linked_list.create_single_linked_list([1,'amine','ezra',15,15241,'JS SUCKS(probably bc i suck at it :)'])
#handle_linked_list.extract_singly_linked_list(root)
root = handle_linked_list.create_doubly_linked_list([1,'amine','ezra',15,15241,'JS SUCKS(probably bc i suck at it :)'])
handle_linked_list.extract_doubly_linked_list(root,1)