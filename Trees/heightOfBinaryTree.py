class Node:
    def __init__(self, k):
        self.key = k
        self.left = None
        self.right = None

def heightBT(root):
    if root==None:
        return 0
    else:
        lh = heightBT(root.left)
        rh = heightBT(root.right)
        return(max(lh, rh)+1)

# driver code:

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left = Node(40)
root.right.right = Node(50)
print(heightBT(root))