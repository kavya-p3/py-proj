class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.left = None
        self.right = None

    def insertLeft(self, data):
        if self.left == None:
            self.left = BinaryTree(data)

        else:
            t = BinaryTree(data)
            t.left = self.left
            self.left = t

    def insertRight(self, data):
        if self.right == None:
            self.right = BinaryTree(data)

        else:
            t = BinaryTree(data)
            t.right = self.right
            self.right = t

    def printTree(self):
        t = self.left
        while (t):
            print(t.key)
            t = t.left

    def insertAt(self, node, data, side):
        root = self.key
        l = self.left
        r = self.right
        while (l):
            if l.key == node:
                if side=='right':
                    temp=l.right
                    s=BinaryTree(data)
                    l.right=s
                    s.right=temp
                    break
                elif side=='left':
                    temp = l.left
                    s = BinaryTree(data)
                    l.left = s
                    s.left = temp
                l=l.left
            else:
                l=l.left

    def getLeftChild(self):
        return self.left

    def getRightChild(self):
        return self.right



def PreOrder(tree):
       if tree :

           print(tree.key)
           PreOrder(tree.getLeftChild())

           PreOrder(tree.getRightChild())

def PostOrder(tree):
    if tree:
        PostOrder(tree.getLeftChild())
        PostOrder(tree.getRightChild())
        print(tree.key)

def InOrder(tree,res):
    if tree:
        InOrder(tree.getLeftChild(),res)
        res.append(tree.key)
        InOrder(tree.getRightChild(),res)

    return res







r = BinaryTree(5)
r.insertLeft(4)
r.insertRight(3)
r.insertRight(2)
r.insertLeft(77)
r.insertRight(9)
r.insertLeft(22)
print(r.right.key)
# #r.insertAt('k','sss','right')
# PreOrder(r)
# print('------------')
PostOrder(r)
# print('---------------')
res=InOrder(r,[])
for i in range(len(res)):
    if res[i]>res[i+1]:
        print('uh-ohh',res[i],res[i+1])
        break

print(res)

