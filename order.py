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
    if val < parent.val: 
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

# Prints in order traversal of BST
def inOrder(parent):
    if parent.left != None:
        inOrder(parent.left)
    
    print(parent.val, end=' ')
    
    if parent.right != None:
        inOrder(parent.right)

# Prints post order traversal of BST
def postOrder(parent):
    if parent.left != None:
        postOrder(parent.left)
    
    if parent.right != None:
        postOrder(parent.right)
    
    print(parent.val, end=' ')

f = open("test", "r")
root = BST(f.readline().strip()) # Creating head of tree
buf = f.readlines()

for x in buf:
    insert(x.strip(), root)

print("Pre order: ", end=' ' )
preOrder(root)
print("")
print("In order: ", end=' ')
inOrder(root)
print("")
print("Post order: ", end=' ')
postOrder(root)
print("")
