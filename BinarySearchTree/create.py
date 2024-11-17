import random
from insert import insert

def create (size):
    if size <= 0:
        return None

    root = None #starting with empty tree

    for _ in range(size):
        random_value = random.randint(1, 50)
        root = insert(root, random_value)

    return root #Retur root of the created Binary Search Number
