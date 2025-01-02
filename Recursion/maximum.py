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
def max(a, b):
    return a if a>= b else b
def findMax(head):
    if head.next == None:
        return head.elem
    maxRest = findMax(head.next)
    return max(head.elem, maxRest)
def FindMax(arr, i):
    if i == len(arr)-1:
        return arr[i]
    maxRest = FindMax(arr, i+1)
    return max(arr[i], maxRest)
def binaryMax(arr, low, high):
    if low == high:
        return arr[low]
    else:
        mid = (low+high)//2
        maxLeft = binaryMax(arr, low, mid)
        maxRight = binaryMax(arr, mid+1, high)
        return max(maxLeft, maxRight)
x = [2, 4,3]
head = createList(x)
print(findMax(head), FindMax(x, 0), binaryMax(x, 0, len(x)-1))