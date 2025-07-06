class Node:
  def __init__(self, data):
    self.data = data
    self.nextValue= None


def traversalNode(headData):
          while headData:
            print(headData.data, end="-->")
            headData = headData.nextValue
          print("null")

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.nextValue = node2
node2.nextValue = node3

traversalNode(node1)
