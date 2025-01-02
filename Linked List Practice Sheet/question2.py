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
def intersection(head1, head2):
    head = None
    temp = None
    temp1 = head1
    temp2 = head2
    while temp1 != None and temp2 != None:
        if temp1.elem == temp2.elem:
            if head == None:
                head = Node(temp1.elem, None)
                temp = head
            else:
                n = Node(temp1.elem, None)
                temp.next = n
                temp = temp.next
            temp1 = temp1.next
            temp2 = head2
        else:
            if temp1.next != None:
                if temp2.next == None:
                    temp2 = head2
                    temp1 = temp1.next
                else:
                    temp2 = temp2.next
            else:
                if temp2.next == None:
                    temp2 = temp2.next
                    temp1 = temp1.next
                else:
                    temp2 = temp2.next
    return head
x = [1, 2, 3, 4, 5]
y = [2, 3, 4]
root1 = createList(x)
root2 = createList(y)
root = intersection(root1, root2)
printList(root)