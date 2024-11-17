import random

#class representing a node in a binary search tree
class Node:
    def __init__(self, value):
        self.value = value #Data that node holds
        self.left = None #refrence to the left child
        self.right = None #refernce to the right child

#creating a class for BinarySearchTree
class BinarySearchTree:
    def __init__(self):
        self.root = None #start with empty root

    def search(self, root, value):
        # Base case: The tree is either empty or the value is found
        if root is None:
            return 'Node not found'
        if root.value == value:  # value matches the current node
            return root
        # if value is smaller search the left subtree
        if value < root.value:
            return self.search(root.left, value)
        # if value is bigger search the right subtree
        else:
            return self.search(root.right, value)


    #Inseerting new value into BST
    def insert(self, root, value):
        # Base case: if tree is empty, create new node
        if root is None:
            return Node(value)
        # if value is smaller go to the left subtree
        if value < root.value:
            root.left =  self.insert(root.left, value)
        # if value is bigger go to the right subtree
        else:
            root.right = self.insert(root.right, value)
        return root  # the updated tree

    def remove(self, root, value):
        #Base case: tree is empty
        if root is None:
            return root

        if value < root.value:
            root.left = self.remove(root.left, value) #Move to left subtree
        elif value > root.value:
            root.right = self.remove(root.right, value) #Move to the right subtree
        else:
            # The Node we wanna delete is found
            # Case 1: Node has no children or leaf node
            if root.left is None and root.right is None:
                return Node

            #Case 2: Node has one child
            elif root.left is None:
                return root.right #Right child replacing the node
            elif root.right is None:
                return root.left #Left child replacing the node

            #Case 3: Node has two children
            else:
                # Find the in-order successor (smallest in the right subtree
                min_node = self._find_min(root.right)
                root.value = min_node,value #Replacing the value of the current node
                #Delete the in-order successor
                root.right = self.remove(root.right, min_node.value)

            return root

        def _find_min(self, root):
            #Helper method to find the minimum value node in the right subtree
            current = root
            while current.left is not None:
                current =  current.left
            return current


    #Creating Automatic BST with random values
    def create(self, size):
        for _ in range(size):
            random_value = random.randint(1, 200)
            self.root = self.insert(self.root, random_value)



#Implemntation and testing part
bst = BinarySearchTree()
print('Creating BST with random values...')
bst.create(20)

#Inserting a specific value
print('\nInserting value 50 into the BST..')
bst.root = bst.insert(bst.root, 50)

#Seraching for a value
print("\n\nSearching for value 50..")
result = bst.search(bst.root, 50)
if isinstance(result, Node):
    print(f'Node found with value: {result.value}')
else:
    print(result)

#Removing a node from BST
bst.root = bst.remove(bst.root, 50)  # Remove node with value 50








