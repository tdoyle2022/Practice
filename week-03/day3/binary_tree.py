class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    
    def __str__(self):
        return f"[{self.value} , {self.left}, {self.right}"
    
myTree = BinaryTree(56, 
                    BinaryTree(22,
                               BinaryTree(10, None, None),
                               BinaryTree(12, None, None)),
                    BinaryTree(81,
                               BinaryTree(77, None, None),
                               BinaryTree(92, None, None)))
    
# def binarySearch(tree, value):
#     currNode = tree
#     while(currNode):
#         if value < currNode.value:
#             currNode = currNode.left
#         elif value > currNode.value:
#             currNode = currNode.right
#         else:
#             return currNode
    
# print(binarySearch(myTree, 4))

# Recurive function
def binarySearch(tree, value):
    if not tree:
        return None
    if value == tree.value:
        return tree
    elif value < tree.value:
        return binarySearch(tree.left, value)
    else:
        return binarySearch(tree.right, value)

print(binarySearch(myTree, 81))

    