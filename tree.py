from collections import deque

class Node:
    def __init__(self,k):
        self.left = None
        self.right = None
        self.data = k

# Driver Code 
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left = Node(40)
root.right.right = Node(60)

treeTraversalString = """
Tree Traversal 
 1. Breadth First 
 2. Depth First
    1. Preorder 
    2. Inorder
    3. Postorder """

def addSeparation():
    print("---------------------------------------------------------")

def preorderTraversal(root):
    if root is not None:
        print(root.data)
        preorderTraversal(root.left)
        preorderTraversal(root.right)

def callPreorderTraversal(root):
    addSeparation()
    print("Preorder Traversal of the Tree")
    print("Root Left Right")
    preorderTraversal(root)

def postorderTraversal(root):
    if root is not None:
        postorderTraversal(root.left)
        postorderTraversal(root.right)
        print(root.data)

def callPostorderTraversal(root):
    addSeparation()
    print("Postorder Traversal of the Tree")
    print("Left Right Root ")
    postorderTraversal(root)

def inorderTraversal(root):
    if root is not None:
        inorderTraversal(root.left)
        print(root.data)
        inorderTraversal(root.right)

def callInorderTraversal(root):
    addSeparation()
    print("Inorder Traversal of the Tree")
    print("Left Root Right ")
    inorderTraversal(root)


def doDFS(root):
    addSeparation()
    print("Depth First")
    callPreorderTraversal(root)
    callPostorderTraversal(root)
    callInorderTraversal(root)


def bfs(root):
    if root is None:
        return 
    q = deque()
    q.append(root)

    while len(q) > 0:
        node = q.popleft()
        print(node.data)

        if node.left is not None:
            q.append(node.left)
        if node.right is not None:
            q.append(node.right)



def callBFSTraversal(root):
    addSeparation()
    bfs(root)


def doBFS(root):
    addSeparation()
    print("Breadth First")
    print("OR")
    print("Level Order Traversal")
    callBFSTraversal(root)


def traverseTree(root):
    addSeparation()
    print(treeTraversalString)
    doDFS(root)
    doBFS(root)

traverseTree(root)
