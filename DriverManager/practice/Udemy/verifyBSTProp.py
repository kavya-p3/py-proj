class Node:
    def __init__(self, data):
        self.key = data
        self.left = None
        self.right = None


def insert(root, data):
    if root == None:
        return Node(data)
    else:
        if root.key == data:
            return root

        elif root.key > data:
            # print(root.key)
            root.left = insert(root.left, data)

        else:
            root.right = insert(root.right, data)
    return root


def verifyBST(root):
  if root:
    p=root.key
    if root.right: r=root.right.key
    else: r=float("inf")
    if root.left:l=root.left.key
    else: l= float("-inf")
    if l<p<r:
        verifyBST(root.right)
        verifyBST(root.left)
        return True
    else:
        print('uh-oh')
        return False


r = Node(5)
insert(r, 4)
insert(r, 0)
insert(r, 6)
insert(r, 2)
insert(r, 1)
insert(r, 3)
insert(r,2.5)
insert(r,3.5)
print(verifyBST(r))
