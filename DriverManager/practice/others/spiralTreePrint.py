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


def spiralPrint(root):
    s1=[root]
    s2=[]
    while s1 !=[] or s2!=[]:
        while s1:
            k = s1.pop()
            if k.left: s2.append(k.left)
            if k.right: s2.append(k.right)
            print(k.key)
        while s2:
            t = s2.pop()
            print(t.key)
            if t.right: s1.append(t.right)
            if t.left: s1.append(t.left)


def treePrint(root):
    if root == None:
        return
    if root.left:
        que.append(root.left)
    if root.right:
        que.append(root.right)
    print((que.pop(0)).key)
    if len(que)!=0:treePrint(que[0])




r = Node(5)

insert(r, 4)
insert(r, 0)
insert(r, 6)
insert(r, 2)
insert(r, 1)
insert(r, 3)
insert(r, 2.5)
insert(r, 3.5)

spiralPrint(r)
print('----------->')
que = [r]
treePrint(que[0])