#a node-an object that has a value in connection to another node
class Node:

    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
