import bst


tree = bst.Node(50)
tree = bst.insert(tree, 25)
tree = bst.insert(tree, 100)
tree = bst.insert(tree, 75)

print(bst.search(tree, 75))
print(bst.search(tree, 999))