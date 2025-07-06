class TreeNode:
    def __init__(self, data):
        self.data = data
        self.rightNode = None
        self.leftNode = None


root = TreeNode('R')
nodeA = TreeNode('A')
nodeB = TreeNode('B')

root.leftNode = nodeA
root.rightNode = nodeB

print(root.rightNode.data)