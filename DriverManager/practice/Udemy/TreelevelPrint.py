# class Node:
#     def __init__(self, data):
#         self.key = data
#         self.left = None
#         self.right = None
#
#
# def insert(root, data):
#     if root == None:
#         return Node(data)
#     else:
#         if root.key == data:
#             return root
#
#         elif root.key > data:
#             # print(root.key)
#             root.left = insert(root.left, data)
#
#         else:
#             root.right = insert(root.right, data)
#     return root


# def treePrint(root):
#     if root == None:
#         return
#     if root.left:
#         que.append(root.left)
#     if root.right:
#         que.append(root.right)
#     print((que.pop(0)).key)
#     if len(que)!=0:
#     treePrint(que[0])
#
#
# def inOrder(root):
#     if root:
#         inOrder(root.left)
#         print(root.key)
#         inOrder(root.right)
#
#
# r = Node(5)
#
# insert(r, 4)
# insert(r, 0)
# insert(r, 6)
# insert(r, 2)
# insert(r, 1)
# insert(r, 3)
# insert(r, 2.5)
# insert(r, 3.5)
# # inOrder(r)
# print('--->')
# que = [r]
# treePrint(que[0])
# Recursive Python program for level order traversal of Binary Tree

# A node structure
class Node:

    # A utility function to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


# Function to print level order traversal of tree
def printLevelOrder(root):
    h = height(root)
    for i in range(1, h + 1):
        printGivenLevel(root, i)


# Print nodes at a given level
def printGivenLevel(root, level):
    if root is None:
        return

    if level == 1:
        print(root.data, end=" ")

    elif level > 1:
        printGivenLevel(root.left, level - 1)
        printGivenLevel(root.right, level - 1)


""" Compute the height of a tree--the number of nodes 
	along the longest path from the root node down to 
	the farthest leaf node 
"""


def height(node):
    if node is None:
        return 0
    else:
        # Compute the height of each subtree
        lheight = height(node.left)
        rheight = height(node.right)

        # Use the larger one
        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1


# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left .left= Node(6)
root.left.right.right = Node(7)
# root.left.left = Node(8)
# root.left.right = Node(9)
# root.left.left = Node(10)
# root.left.right = Node(11)


print("Level order traversal of binary tree is -")
printLevelOrder(root)
