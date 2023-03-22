
class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.value = key


def insert(root,key):
    if root is None: # base case
        return Node(key) # insert node
    else:
        if root.value == key:
            return root # no duplicate values
        elif root.value < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root


def search(root,key):
    if root is None or root.value == key:
        return root
    
    if root.value < key:
        return search(root.right, key)
    
    return search(root.left, key)


def print_in_order(root, output):
    output += "," + str(root.value)

    return output