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
def seqSearch(head, item):
    if head == None:
        return False
    if head.elem == item:
        return True
    return seqSearch(head.next, item)
def sequence(arr,i, item):
    if i >= len(arr):
        return False
    if arr[i] == item:
        return True
    return sequence(arr,i+1, item)
x = [1,2,3,4]
head = createList(x)
print(sequence(x,0, 4))
print(sequence(x,0, 14))
print(seqSearch(head, 4))
print(seqSearch(head, 14))