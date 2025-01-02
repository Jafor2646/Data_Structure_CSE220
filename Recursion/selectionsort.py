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
def swapNode(a, b):
    temp = a.elem
    a.elem = b.elem
    b.elem = temp
def swapArr(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp
def findMinNode(head):
    if head.next == None:
        return head
    minNode = head
    minNodeNext = findMinNode(head.next)
    if(minNode.elem > minNodeNext.elem):
        minNode = minNodeNext
    return minNode
def findMinIdx(arr, low, high):
    if low == high:
        return low
    else:
        mid = (low+high)//2
        minIdxLeft = findMinIdx(arr, low, mid)
        minIdxRight = findMinIdx(arr, mid+1,high)
        minIdx = minIdxLeft
        if arr[minIdxLeft] > arr[minIdxRight]:
            minIdx = minIdxRight
        return minIdx
def selectionSort(arr, i):
    if i == len(arr)-1:
        return
    minIdx = findMinIdx(arr, i, len(arr)-1)
    swapArr(arr, i, minIdx)
    selectionSort(arr, i+1)
def selectionsort(head):
    if head == None or head.next == None:
        return
    minNode = findMinNode(head)
    swapNode(head, minNode)
    selectionsort(head.next)
x = [7, 4, 6, 5, 9, 3, 8, 12, 10]
head = createList(x)
selectionSort(x, 0)
selectionsort(head)
print(x)
printList(head)