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
def evenToOdd(head):
    h=head
    newHead,temp = None,None
    while h!=None:
        if h.elem%2==0:
            if newHead==None:
                newHead=Node(h.elem,None)
                temp = newHead
            else:
                temp.next = Node(h.elem,None)
                temp=temp.next
        h = h.next
    h=head
    while h!=None:
        if h.elem%2==1:
            temp.next=Node(h.elem,None)
            temp=temp.next
        h=h.next
    return newHead
lst = [17,15,8,12,10,5,4,1,7,6]
head = createList(lst)
printList(head)
newHead = evenToOdd(head)
printList(newHead)