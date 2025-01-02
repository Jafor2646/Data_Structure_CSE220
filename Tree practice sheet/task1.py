class Node:
    def __init__(self, e):
        self.elem = e
        self.left = None
        self.right = None
def treeCronstuctor(arr, i , n):
    root = None
    if i < n:
        if arr[i] != None:
            root = Node(arr[i])
            root.left = treeCronstuctor(arr, 2*i+1, n)
            root.right = treeCronstuctor(arr, 2*i+2, n)
    return root
def printInorder(root):
    if root != None:
        printInorder(root.left)
        print(root.elem, end=" ")
        printInorder(root.right)
x = ['a','b','c','d','e','f', 'g','h',None,None,None, 'i', 'j', None, 'k']
root = treeCronstuctor(x, 0, len(x))
printInorder(root)
def isMirror(root1, root2):
    if root1 == None and root2 == None:
        return True
    if root1 == None or root2 == None:
        return False
    return (root1.elem == root2.elem) and isMirror(root1.left, root2.right) and isMirror(root1.right, root2.left)
def issymetric(root):
    if root == None:
        return True
    return isMirror(root.left, root.right)
print()
print(issymetric(root))