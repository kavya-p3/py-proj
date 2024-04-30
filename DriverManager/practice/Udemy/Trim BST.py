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


def removeOutsideRange(root, min, max):
    # Base Case
    if root == None:
        return None

    # First fix the left and right
    # subtrees of root
    root.left = removeOutsideRange(root.left, min, max)
    root.right = removeOutsideRange(root.right, min, max)

    # Now fix the root. There are 2
    # possible cases for toot
    # 1.a) Root's key is smaller than
    #      min value (root is not in range)
    #print(root.key)
    if root.key < min:
        return root.right

    # 1.b) Root's key is greater than max
    #      value (root is not in range)
    if root.key > max:
        return root.left

        # 2. Root is in range
    return root


def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.key)
        inOrder(root.right)


r = Node(5)

insert(r, 4)
insert(r, 0)
insert(r, 6)
insert(r, 2)
insert(r, 1)
insert(r, 3)
insert(r, 2.5)
insert(r, 3.5)
# inOrder(r)

k = removeOutsideRange(r, 2, 4)
# print('----->')
inOrder(k)
# print('rootis ',k.key)
