class Node:
    def __init__(self, k):
        self.key = k
        self.left = None
        self.right = None

def treesize(root):
    if root==None:
        return 0
    else:
        ls = treesize(root.left)
        rs = treesize(root.right)
        return(ls+rs+1)


# driver code:

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left = Node(40)
root.right.right = Node(50)
print(treesize(root))