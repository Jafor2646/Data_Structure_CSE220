class Node:
    def __init__(self, elem, next):
        self.val = elem
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
            print(temp.val)
        else:
            print(temp.val,end="->")
        temp = temp.next
def reverseKGroup(head, k):
    if k == 1:
        return head
    temp = head
    new_head = head
    start, end, nextNode, prev_node_temp, prev_node = None, None, None, None, None
    flag = False
    count = 0
    check = 0
    while temp != None:
        if start == None:
            prev_node = prev_node_temp
            start = temp
            check += 1
        elif check != k:
            end = temp
            check += 1
        else:
            if end != None:
                nextNode = end.next
            if start == head:
                new_head = end
            temp1 = start
            temp_head = None
            while temp1 != nextNode:
                n = temp1.next
                temp1.next = temp_head
                temp_head = temp1
                temp1 = n
            if start != head:
                prev_node.next = end
            start.next = nextNode
            prev_node_temp = start
            start = None
            end = None
            check = 0
            flag = True
        if flag:
            flag = False
        else:
            prev_node_temp = temp
            temp = temp.next
        count += 1
    if start != None and end != None and check == k and k == count:
        temp = head
        new_head = None
        while temp != None:
            n = temp.next
            temp.next = new_head
            new_head = temp
            temp = n
    elif start != None and end != None and check == k:
        temp_head = None
        temp1 = start
        while temp1 != None:
            n = temp1.next
            temp1.next =temp_head
            temp_head = temp1
            temp1 = n
        prev_node.next = end
    return new_head

x = [1, 2, 3, 4, 5]
root = createList(x)
printList(root)
newRoot = reverseKGroup(root, 2)
printList(newRoot)