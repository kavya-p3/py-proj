class BinaryTree:
    def __init__(self, data):
        self.key = data
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

    def getLeftChild(self):
        return self.left

    def getRightChild(self):
        return self.right


def invertTree(tree):
     if not tree :
         return
     tree.left,tree.right=tree.right,tree.left
     invertTree(tree.left)
     invertTree(tree.right)



def InOrder(tree):
    if tree:
        InOrder(tree.left)
        print(tree.key)
        InOrder(tree.right)



r=BinaryTree(5)
r.insertLeft(6)
r.insertLeft(7)
r.insertLeft(8)
r.insertRight(10)
InOrder(r)
print('------->')
invertTree(r)
InOrder(r)

