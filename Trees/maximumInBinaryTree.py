import math
class Node:
    def __init__(self, k):
        self.key = k
        self.left = None
        self.right = None

def maxm(root):
    if root==None:
        return -math.inf
    else:
        ls = maxm(root.left)
        rs = maxm(root.right)
        return(max(root.key, ls, rs))

# driver code:

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left = Node(40)
root.right.right = Node(50)
print(maxm(root))