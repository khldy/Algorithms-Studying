class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key


class BST:
    def __init__(self):
        self.root = None

    # Insert a new node with a given value
    def insert(self, root, key):
        if root is None:
            return Node(key)

        if key < root.value:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        return root

    # Search for a value in th tree
    def search(self, root, key):
        if root is None or root.value == key:
            return root
        if key < root.value:
            return self.search(root.left, key)

        return self.search(root.right, key)
    # Inorder Traversal (Left, Root, Right)
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.value, end = "")
            self.inorder(root.right)

    # Preorder Traversal (Root, Left, Right)
    def preorder (self, root):
        if root:
            print(root.value, end = "")
            self.preorder(root.left)
            self.preorder(root.right)

    # Postorder Traversal (Left, Right, Root)
    def postorder (self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.value, end = "")

    # Delete a node with a given value
    def delete(self, root, key):
        if root is None:
            return root

        # Traverse the tree
        if key < root.value:
            root.left = self.delete(root.left, key)
        elif key > root.value:
            root.right = self.delete(root.right, key)
        else:
            # Case 1: Node has no children (leaf node)
            if root.left is None and root.right is None:
                return None

            # Case 2: Node has one child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Case 3: node has two children
            min_node = self.min_value_node(root.right)
            root.value = min_node.value
            root.right = self.delete(root.right, min_node.value)

        return root

    def min_value_node(selfself, root):
        current = root
        while current.lrft is not None:
            current = current.left
        return current

# Driver code to demonstrate BST
bst = BST()
root = None
values = [20, 8, 22, 4, 12, 10, 14]

for value in values:
    root = bst.insert(root, value)

print('Inorder Traversal: ')
bst.inorder(root)

print('\nPreorder Traversal: ')
bst.preorder(root)

print('\nPostorder Traversal: ')
bst.postorder(root)

search_result = bst.search(root, 10)
if search_result:
    print('\nValue 10 found in the tree.')
else:
    print('\nValue 10 not found i nthe tree.')

