class Node:
    def __init__(self,elem,n=None):
        self.elem=elem
        self.next=n
class LinkedList:
    def __init__(self,a,b):
        self.head1=None
        tail=self.head1
        if len(a)!=0:
            if len(a)==1:
                self.head1=Node(a[0],None)
                tail=self.head1
            else:
                self.head1=Node(a[0],None)
                #print(self.head)
                tail1=self.head1
                for i in range(1,len(a)):
                    nxt1=Node(a[i],None)
                    print(nxt1.elem)
                    tail1.next=nxt1
                    tail1=nxt1
        if len(b)!=0:
            if len(b)==1:
                self.head2=Node(b[0],None)
                tail2=self.head2
            else:
                self.head2=Node(b[0],None)
                #print(self.head)
                tail2=self.head2
                for i in range(1,len(b)):
                    nxt2=Node(b[i],None)
                    print(nxt2.elem)
                    tail2.next=nxt2
                    tail2=nxt2
                    
    def printlist(self):
        head1=self.head1
        while head1!=None:
            if head1.next!=None:
                print(head1.elem, end=",")
            else:
                print(head1.elem)
            head1=head1.next
        head2=self.head2
        while head2!=None:
            if head2.next!=None:
                print(head2.elem, end=",")
            else:
                print(head2.elem)
            head2=head2.next
    
    def intersec(self):
        tail1=self.head1
        tail2=self.head2
        temp=None
        tail=None
        while tail1!=None:
            while tail2!=None:
                if tail1.elem==tail2.elem:
                    if temp!=None:
                        temp=Node(tail1.elem,None)
                        tail=temp
                    else:
                        n=Node(tail1.elem,None)
                        temp.next=n
                        tail=tail.next
                    break
                tail2=tail2.next        
            tail1=tail1.next
        return temp
                        
                    
a=[1,2,3,4,6]
b=[2,4,6]
obj1=LinkedList(a,b)
obj1.printlist()
print("==============")