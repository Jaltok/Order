# !/usr/bin/python3
# Copyright (c) 2018 Jeff Lund

# Node class of binary search tree
class BST(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(val, parent):
    if val == parent.val:
        return
    elif val < parent.val: 
        if parent.left:
            insert(val, parent.left)
        else:
            parent.left = BST(val)
    else: 
        if parent.right:
            insert(val, parent.right)
        else:
            parent.right = BST(val)

# Prints pre order traversal of BST
def preOrder(parent):
    print(parent.val, end=' ')
    if parent.left != None:
        preOrder(parent.left)
    if parent.right != None:
        preOrder(parent.right)
    return

# Prints in order traversal of BST
def inOrder(parent):
    if parent.left != None:
        inOrder(parent.left)
    print(parent.val, end=' ')
    if parent.right != None:
        inOrder(parent.right)
    return

# Prints post order traversal of BST
def postOrder(parent):
    if parent.left != None:
        postOrder(parent.left)
    if parent.right != None:
        postOrder(parent.right)
    print(parent.val, end=' ')
    return

def printLeft(parent):
    while(parent.left != None):
        parent = parent.left
    print("Left most value is: ")
    print(parent.val)
   
def printRight(parent):
    while(parent.right != None):
        parent = parent.right
    print("Right most value is: ")
    print(parent.val)
    return

f = open("test", "r")
root = BST(int(f.readline().strip())) # Creating head of tree
buf = f.readlines()

for x in buf:
    insert(int(x.strip()), root)

printLeft(root)
printRight(root)
print("Printing Tree")

print("Pre order: ", end=' ' )
preOrder(root)
print("")
print("In order: ", end=' ')
inOrder(root)
print("")
print("Post order: ", end=' ')
postOrder(root)
print("")
