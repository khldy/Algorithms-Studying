from node import Node

def insert(root, value):
    # Base case: if tree is empty, create new node
    if root  == None:
        return Node(value)

    #if value is smaller go to the left subtree
    if value < root.value:
        return insert(root.left, value)
    #if value is bigger go to the right subtree
    if value > root.value:
        return insert(root.right, value)

    return root #the updated tree