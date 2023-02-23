class BinaryTree:
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right
    def __str__(self):
        return f"[{self.value}, {self.left}, {self.right}]"

my_tree = BinaryTree(50,
                    ## LEFT SIDE
                    BinaryTree(25,
                                BinaryTree(10, None, None),
                                BinaryTree(40,
                                          BinaryTree(15, None, None))),
                    # RIGHT SIDE
                    BinaryTree(75,
                                #LEFT SIDE
                               BinaryTree(60, None, None),
                               # RIGHT SIDE
                               BinaryTree(80,
                                            BinaryTree(70, None, None),
                                            BinaryTree(90, None, None)))
                                            )

def binarySearch(tree,value):
    currentNode = tree
    while(currentNode):
        if value < currentNode.value:
            currentNode = currentNode.left
        elif value > currentNode.value:
            currentNode = currentNode.right
        else: return currentNode
print(binarySearch(my_tree,25))