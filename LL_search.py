# Program for searching an element in the linked list

def search(head, x):
    pos = 1
    curr = head
    while curr!= None:
        if curr.key == x:
              return pos
        pos +=1
        curr = curr.next

    return -1




