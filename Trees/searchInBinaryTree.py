class Node:
    def __init__(self, k):
        self.key = k
        self.left = None
        self.right = None

def searchBT(root, key):
    if root is None:
        return False
    elif root.key ==key:
        return True
    elif searchBT(root.left, key):
        return True
    elif searchBT(root.right, key):
        return True
    else: return False
    

def sea(root, key):
    if root is None:
        return False
    elif root.key == key or searchBT(root.left, key) or searchBT(root.right, key):
        return True
    else:
        return False
# driver code:

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left = Node(40)
root.right.right = Node(50)


# funiton call

print(searchBT(root, 00))
print(sea(root, 0))