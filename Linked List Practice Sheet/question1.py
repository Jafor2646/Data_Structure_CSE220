class Node:
    def __init__(self, elem, next):
        self.elem = elem
        self.next = next
def createList(a):
    head = Node(a[0], None)
    tail = head
    for i in range(1, len(a)):
        n = Node(a[i], None)
        tail.next = n
        tail = tail.next
    return head
def printList(head):
    temp = head
    while temp != None:
        if temp.next == None:
            print(temp.elem)
        else:
            print(temp.elem,end="->")
        temp = temp.next
def lastNodeToTheFront(head):
    temp = head
    while temp.next.next != None:
        temp = temp.next
    temp.next.next = head
    head = temp.next
    temp.next = None
    return head
x = [3, 8, 1, 5, 7, 12]
root = createList(x)
printList(root)
rs = lastNodeToTheFront(root)
printList(rs)

