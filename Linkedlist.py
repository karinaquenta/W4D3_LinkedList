#linked list
#store every element in its own allocation
#its a collection of elements
from Node import Node
class LinkedList:
    
    def __init__(self):
        self.head = None

    def add_node(self, value): #adding to end of list
        node = Node(value)
        if not self.head:
          self.head = node #sunday
        else: #stops our metohds
          current_node = self.head #sunday
          while current_node.right: #condition is false
             print(current_node.value)
             current_node = current_node.right
          current_node.right = node #sunday, right attribute as Monday
#dont ever need to call this, iterate thru linked list
    def __iter__(self): #we will have access to all nodes, prints all
       current_node = self.head #create a list to store nodes & thats what we will iterate thru
       while current_node: #we will loop til we run out of nodes
          yield current_node #yield is a generator, creating a generator object, store every element, can loop thru a yield
          current_node = current_node.right

          #FLASK week-magic methods
    def __repr__(self):
       nodes = []
       for node in self:
          nodes.append(node.value)
       return '-->'.join(nodes)
              
    def insert_node(self, target, value):
       new_node = Node(value) #make value a node
       if self.head:
          for node in self: #lets loop til we find our target(below)
             if node.value == target: #found tues
                right_node = node.right #dont want to lose the node, store it
                node.right = new_node #overwite right attribute
                new_node.right = right_node
       else:
         print('Empty List')

             
    def remove_node(self,value): #chopping off Monday
       if value == self.head.value:
          self.head = self.head.right #reassiginig to heads right
       else:
          for node in self: #sunday
             if node.right.value == value:  #if node right attribute is th one i want to remove, then overwite nodes.right to the next nodes right
                node.right = node.right.right 
                return

    def insert_prior(self, target, value):
       new_node = Node(value) #make value a node
       if self.head:
          for node in self: #lets loop til we find our target(below)
             if node.right.value == target: #found tues
                right_node = node.right #dont want to lose the node, store it
                node.right = new_node #overwite right attribute
                new_node.right = right_node
                return
       else:
         print('Empty List')

    #return the last one 
    def get_tail(self):
    #    for node in self:
    #       pass
    #    return node.value
        node = self.head
        while node.right:
            node = node.right
        return node.value

    #remove tail
    def remove_tail(self):
        node = self.head
        if node.right:
            while node.right.right:
                node = node.right
            node.right = None   



linked_list = LinkedList()

linked_list.add_node('Sunday')
linked_list.add_node('Monday')
linked_list.add_node('Tuesday')#need to insert wed
linked_list.add_node('Thursday')
#print(linked_list.head.right.value)
#print(linked_list)
linked_list.insert_node('Tuesday', "Wednesday")

linked_list.add_node('spazzday')
linked_list.remove_node("Sunday")
linked_list.remove_node("spazzday")
print(linked_list)

linked_list.insert_prior('Tuesday', 'Sunday')
print(linked_list)

linked_list.remove_tail

#--------
from Node import Node

class LinkedList:
    
    def __init__(self):
        self.head = None

    def add_node(self, value):
        node = Node(value)
        if not self.head:
          self.head = node
        else:
          current_node = self.head
          while current_node.right:
              current_node = current_node.right
          current_node.right = node

    def __iter__(self):
       current_node = self.head
       while current_node:
          yield current_node
          current_node = current_node.right

    def __repr__(self):
      return ' -> '.join(node.value for node in self)
      # nodes = []
      # for node in self:
      #   nodes.append(node.value)
      # return ' -> '.join(nodes)

    def insert_node(self, target, value):
       new_node = Node(value)
       if self.head:
          for node in self:
             if node.value == target:
                right_node = node.right
                node.right = new_node
                new_node.right = right_node
       else:
          print('Empty List')





# Dylan Smith [Staff]
#   21 minutes ago
# Updated Linked List
from Node import Node

class LinkedList:
    
    def __init__(self):
        self.head = None

    def add_node(self, value):
        node = Node(value)
        if not self.head:
          self.head = node
        else:
          current_node = self.head
          while current_node.right:
              previous_node = current_node
              current_node = current_node.right
              current_node.left = previous_node
          current_node.right = node

    def __iter__(self):
       current_node = self.head
       while current_node:
          yield current_node
          current_node = current_node.right

    def __repr__(self):
      return ' -> '.join(node.value for node in self)
      # nodes = []
      # for node in self:
      #   nodes.append(node.value)
      # return ' -> '.join(nodes)

    def insert_node(self, target, value):
       new_node = Node(value)
       if self.head:
          for node in self:
             if node.value == target:
                right_node = node.right
                node.right = new_node
                new_node.right = right_node
       else:
          print('Empty List')

    def remove_node(self, value):
        if value == self.head.value:
           self.head = self.head.right
        else:
           for node in self:
              if node.right:
                if node.right.value == value:
                  node.right = node.right.right
                  return
                
    def get_tail(self):
      #  for node in self:
      #     pass
      #  return node.value
      node = self.head
      while node.right:
         node = node.right
      return node.value

    def remove_tail(self):
      node = self.head
      if node.right:
        while node.right.right:
          node = node.right
        node.right = None