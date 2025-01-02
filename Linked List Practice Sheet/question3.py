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
def reverseEvenNumber(head):
    temp = head
    new_head = head
    start, end, nextNode, prev_node_temp,prev_node = None, None, None, None, None
    while temp != None:
        if temp.elem % 2 == 0 and start == None:
            prev_node = prev_node_temp
            start = temp
        elif temp.elem % 2 == 0 and start != None:
            end = temp
        elif temp.elem % 2 == 1 and start != None and end != None:
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
            start = None
            end = None
        elif temp.elem % 2 == 1 and end == None:
            start = None
        prev_node_temp = temp
        temp = temp.next
    if start != None and end != None:
        temp_head = None
        temp1 = start
        while temp1 != None:
            n = temp1.next
            temp1.next =temp_head
            temp_head = temp1
            temp1 = n
        prev_node.next = end
    return new_head
x = [2, 18, 24, 3, 5, 7, 9, 6, 12, 43, 45, 22, 23, 12, 32, 46, 65, 14, 22, 66, 88, 86]
head1 = createList(x)
printList(head1)
head2 = reverseEvenNumber(head1)
printList(head2)