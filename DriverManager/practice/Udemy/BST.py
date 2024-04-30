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


def minsuccessor(root):
    while root.left :
        root=root.left

    return root


def delNode(root, data):
    if root == None:
        return root
    else:
        if root.key == data:
            if root.right == None:
                temp=root.left
                #root= None
                return temp

            if root.left == None:
                temp= root.right
                #root=None
                return temp

            tem = minsuccessor(root.right)
            root.key=tem.key
            root.right= delNode(root.right,tem.key)
            return root

        else:
            if data > root.key:
                root.right = delNode(root.right, data)
            else:
                root.left = delNode(root.left, data)
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
insert(r,2.5)
insert(r,3.5)
inOrder(r)
print('--->')
delNode(r, 6)
inOrder(r)
