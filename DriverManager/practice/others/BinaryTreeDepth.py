ans = 0
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


def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.key)
        inOrder(root.right)





def depth(root, dep):
    global ans
    ans+=dep
    if root.left:
        depth(root.left,dep+  1)
    if root.right:
        depth(root.right,dep+ 1)
    print(ans)


r = Node(5)

insert(r, 4)
insert(r, 7)
insert(r, 6)
insert(r, 8)
insert(r, 3)
insert(r, 4.5)
insert(r, 2.5)
insert(r, 3.6)
# inOrder(r)
depth(r, 0)
