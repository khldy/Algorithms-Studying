def search(root ,value):
    # Base case: The tree is either empty or the value is found
    if root == None:
        return 'Node not found'
    if root.value == value: #vlaue matches the current node
        return root

    #if value is smaller search the left subtree
    if value < root.value:
        return search(root.left, value)
    #if value is bigger search the right subtree
    if value > root.value:
        return search(root.right, value)