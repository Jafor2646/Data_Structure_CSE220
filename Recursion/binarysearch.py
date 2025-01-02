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
def binarysearch(arr,low, high, item):
    if low>high:
        return False
    mid = (low+high)//2
    if arr[mid] == item:
        return True
    elif item > arr[mid]:
        return binarysearch(arr,low+1,high, item)
    else:
        return binarysearch(arr, low, high-1,item)
x = [1,2,3,4]
print(binarysearch(x,0,len(x)-1, 4))
print(binarysearch(x,0,len(x)-1, 14))